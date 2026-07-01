from django.urls import path 
from .views import AgencyListView, AgencyDetailView, create_review_view

urlpatterns = [
    path("", AgencyListView.as_view(), name="agency_list"),
    path("<int:pk>/", AgencyDetailView.as_view(), name="agency_detail"),
    path("<int:pk>/review/", create_review_view, name="create_review"),
]