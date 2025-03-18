from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Categoria

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email", "password"]
        widgets = {
            "username": forms.TextInput(attrs={"placeholder": "Usuario", "required": True}),
            "email": forms.EmailInput(attrs={"placeholder": "Email", "required": True}),
            "password": forms.PasswordInput(attrs={"placeholder": "Contraseña", "required": True}),
        }
        
class CatForm(ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'description']