from django.forms import ModelForm
from .models import Tecnico, Equipo, Alistamiento, DiagnosticoEquipos, InsumosTecnicos, HerramientaTecnicos
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class EquipoForm(ModelForm):
    class Meta:
        model = Equipo
        fields = '__all__'
        widgets = {
            'update': forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'}
            )
        }

class AlistamientoForm(ModelForm):
    class Meta:
        model = Alistamiento
        fields = '__all__'
        widgets = {
            'update': forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'}
            )
        }

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields }


class DiagnosticoForm2(ModelForm):
    class Meta:
        model = DiagnosticoEquipos
        fields = '__all__'
        widgets = {
            'update': forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'}
            )
        }

class InsumosTecnicoForm(ModelForm):
    class Meta:
        model = InsumosTecnicos
        fields = '__all__'
        widgets = {
            'fecha': forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'}
            )
        }

class HerramientaForm(ModelForm):
    class Meta:
        model = HerramientaTecnicos
        fields = '__all__'
        widgets = {
            'fecha': forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'}
            )
        }
