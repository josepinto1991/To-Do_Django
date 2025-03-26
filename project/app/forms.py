from django import forms
from .models import Task
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TaskForm(forms.ModelForm):
    
    task = forms.CharField(required=True, label="Tarea", widget=forms.Textarea(attrs={'placeholder': 'Escribe tu tarea aquí...'}))
    class Meta:
        model = Task
        fields = ['task']

# Formulario de inicio de sesión (recomendado usar AuthenticationForm)
class LoginForm(forms.Form):
    username = forms.CharField(required=True, label="Nombre de usuario")
    password = forms.CharField(widget=forms.PasswordInput, required=True,label="Contraseña")
    
    class Meta:
        model = User
        fields = ['username', 'password']

# Formulario de registro
class RegisterForm(UserCreationForm):
    username = forms.CharField(label="Nombre de usuario", required=True)
    email = forms.EmailField(label="Correo", required=True)
    password1 = forms.CharField(widget=forms.PasswordInput, label="Contraseña", required=True)
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirmar contraseña", required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    