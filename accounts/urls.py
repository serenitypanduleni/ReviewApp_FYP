from django.urls import path 
from .import views 
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("verify-code/", views.verify_code, name="verify_code"),
    path("login/", auth_views.LoginView.as_view(template_name="accounts/login.html"), name="login"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]