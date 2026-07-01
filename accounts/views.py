# Reference - https://docs.djangoproject.com/en/6.0/topics/http/sessions/#:~:text=flush()¶&text=Deletes%20the%20current%20session%20data,contrib.

from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, VerificationCodeForm
from django.contrib.auth import login, authenticate
from .services import send_verification_code, check_verification_code
from .models import UserModel
from django.contrib.auth.decorators import login_required
from reviews.models import Agency


# User registration view
def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            send_verification_code(user.phone_number)
            request.session["user_id"] = user.id

            return redirect("verify_code")
    else:
        form = UserRegistrationForm()
    return render(request, "accounts/register.html", {"form": form})


# Code verification view
def verify_code(request):
    user_id = request.session.get("user_id")
    if not user_id:
        return redirect("register")
    user = UserModel.objects.get(id=user_id)

    if request.method == "POST":
        form = VerificationCodeForm(request.POST)
        if form.is_valid():
            verification_code = form.cleaned_data["code"]
            if check_verification_code(user.phone_number, verification_code):
                user.is_active = True
                user.is_number_verified = True
                user.save()

                login(request, user)

                return redirect("dashboard")
    else:
        form = VerificationCodeForm()
    return render(request, "accounts/verify_code.html", {"form": form})


# Login view
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("dashboard")
    return render(request, "registration/login.html")


# User and Admin dashboard view
@login_required
def dashboard(request):
    agency_list = Agency.objects.all()
    if request.user.user_role == "admin":
        return render(request, "accounts/admin_dashboard.html")
    else:
        return render(
            request, "accounts/user_dashboard.html", {"agency_list": agency_list}
        )
