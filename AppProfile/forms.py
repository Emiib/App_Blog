from cProfile import label
from django import forms
#formulario de django para crear usuarios
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#lo traigo para el formulario de avatar
from .models import Avatar



#formulario de creacion de usuario
class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(label='Nombre', required=False)
    last_name = forms.CharField(label='Apellido', required=False)
    username = forms.CharField(label='Usuario', required=True)
    email = forms.EmailField(label='email')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Reingrese contraseña', widget=forms.PasswordInput)
    mybio = forms.CharField(max_length=150, label='Description')
    instagram_rss = forms.URLField(max_length=32, label='Instagram', required=False)
    github_rss = forms.URLField(max_length=32, label='Github', required=False)
    linkedin_rss = forms.URLField(max_length=32, label='Linkedin', required=False)
    

    class Meta:
        model = User
        fields = ['username','email', 'password1','password2']
        help_texts = {k:"" for k in fields}

#formulario de actualizacion de usuario
class UpdateProfileForm(UserCreationForm):
    
    username = forms.CharField(label='New Username', required=False)
    email = forms.EmailField(label='email')
    first_name = forms.CharField(label='Update Name', required=False)
    last_name = forms.CharField(label='Update Lastname', required=False)    
    password1 = forms.CharField(label='New Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repet Password', widget=forms.PasswordInput)
    mybio = forms.CharField(max_length=150, label='Description',required=False)
    instagram_rss = forms.URLField(max_length=32, label='Instagram',required=False)
    github_rss = forms.URLField(max_length=32, label='Github',required=False)
    linkedin_rss = forms.URLField(max_length=32, label='Linkedin',required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        help_texts = {k:"" for k in fields}  

#trae del .models para crear el formulario de avatar
class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['avatar',] 