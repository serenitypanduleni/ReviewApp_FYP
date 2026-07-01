from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

class UserModel(AbstractUser):
    USER_ROLES = [("user", "User"),("admin", "Admin")]
    email = models.EmailField(unique=True, blank=False)
    phone_number = PhoneNumberField(region="GB", unique=True, blank=False)
    is_number_verified = models.BooleanField(default=False)
    user_role = models.CharField(max_length=10, choices=USER_ROLES, default="user")

    def __str__(self):
        return self.username 



