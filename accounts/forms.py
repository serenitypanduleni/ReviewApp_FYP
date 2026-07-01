from django import forms 
from django.contrib.auth.forms import UserCreationForm
from .models import UserModel 

# User registration form
class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ["username", "first_name", "last_name", "email", "phone_number"]

class VerificationCodeForm(forms.Form):
    code = forms.CharField(max_length=6, required=True)


