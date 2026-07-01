from django.contrib import admin
from .models import Agency, Review

class ReviewInline(admin.TabularInline):
    model = Review

class AgencyAdmin(admin.ModelAdmin):
    inlines = [
        ReviewInline,
    ]
    list_display = ("agency_name", "description")

class ReviewAdmin(admin.ModelAdmin):
    list_display = ("user", "review_text", "review_rating", "agency", "predicted_sentiment", "is_flagged")

admin.site.register(Agency, AgencyAdmin)
admin.site.register(Review, ReviewAdmin)
