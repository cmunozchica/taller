from django.forms import ModelForm
from .models import Tecnico, Equipo1, Cliente, NumParte, Alistamiento, Modelo, Marca, ManualParte, RepuestoTaller, ManualServicio
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class TecnicoForm(ModelForm):
    class Meta:
        model = Tecnico
        fields = '__all__'

class EquipoForm(ModelForm):
    class Meta:
        model = Equipo1
        fields = '__all__'

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class NumParteForm(ModelForm):
    class Meta:
        model = NumParte
        fields = '__all__'

class AlistamientoForm(ModelForm):
    class Meta:
        model = Alistamiento
        fields = '__all__'

class MarcaForm(ModelForm):
    class Meta:
        model = Marca
        fields = '__all__'

class modeloForm(ModelForm):
    class Meta:
        model = Modelo
        fields = '__all__'

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields }

class ManualPartesForm(ModelForm):
    class Meta:
        model = ManualParte
        fields = '__all__'

class ManualServicioForm(ModelForm):
    class Meta:
        model = ManualServicio
        fields = '__all__'

class RepuestoTallerForm(forms.ModelForm):
    class Meta:
        model = RepuestoTaller
        fields= '__all__'
