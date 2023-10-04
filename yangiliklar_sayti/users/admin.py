from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCteationForm,CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCteationForm
    form = CustomUserChangeForm
    models = CustomUser
    list_display = ['email','username','age','address','job','tel']

admin.site.register(CustomUser,CustomUserAdmin)