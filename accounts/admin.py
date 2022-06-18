from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
  add_form = CustomUserCreationForm
  change_form = CustomUserChangeForm
  model = CustomUser
  list_display = [
    'username',
  ]

admin.site.register(CustomUser, CustomUserAdmin)
