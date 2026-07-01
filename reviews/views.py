from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Agency, Review
from .forms import CreateReviewForm
from sentiment.services import predict_sentiment, check_mismatch
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name="dispatch")
class AgencyListView(ListView):
    model = Agency
    context_object_name = "agency_list"
    template_name = "reviews/agency_list.html"

@method_decorator(login_required, name="dispatch")
class AgencyDetailView(DetailView):
    model = Agency
    context_object_name = "agency"
    template_name = "reviews/agency_detail.html"

    

@login_required
def create_review_view(request, pk):
    agency = get_object_or_404(Agency, pk=pk)
    if request.method == "POST":
        form = CreateReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            if review.review_rating == 3:
                review.save()
            else:
                review.agency = agency
                review.user = request.user
                review.predicted_sentiment = predict_sentiment(review.review_text)
                review.is_flagged = check_mismatch(review.predicted_sentiment, review.review_rating)
                print(review.is_flagged)
                review.save()
            return redirect("agency_detail", pk=agency.id)
    else:
        form = CreateReviewForm
    return render(request, "reviews/create_review.html", {"form": form})

