from django.db import models
from django.conf import settings
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
    MinLengthValidator,
)
from django.urls import reverse


class Agency(models.Model):
    agency_name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.agency_name

    def get_abslute_url(self):
        return reverse("agency_detail", args=[str(self.id)])

    def get_overall_sentiment(self):
        positive_reviews = self.reviews.filter(predicted_sentiment="positive").count()
        negative_reviews = self.reviews.filter(predicted_sentiment="negative").count()

        if positive_reviews > negative_reviews:
            return "Positive"
        elif positive_reviews < negative_reviews:
            return "Negative"
        else:
            return "Neutral"


class Review(models.Model):
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    review_text = models.TextField(validators=[MinLengthValidator(100)])
    review_rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    predicted_sentiment = models.CharField(max_length=12, blank=True)
    is_flagged = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.review_text
