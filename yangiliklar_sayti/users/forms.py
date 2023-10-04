from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import CustomUser

class CustomUserCteationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields+('email','age','address','job','tel')

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        models = CustomUser
        fields = UserChangeForm.Meta.fields
