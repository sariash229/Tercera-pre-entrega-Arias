from django import forms
from django.forms import ModelForm, Textarea
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User

from .models import Materia
from .models import Semestre

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label= 'Correo')
    password1 = forms.CharField(label = 'Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label = 'Confirma Contraseña', widget=forms.PasswordInput)
    
    
    class Meta:
        model = User
        fields =['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}
        
class MateriaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args,**kwargs)
        self.fields['nombreMateria'].widget.attrs.update({'class': 'form-control'})
        self.fields['nombreProfesor'].widget.attrs.update({'class': 'form-control'})
        self.fields['semestre'].widget.attrs.update({'class': 'form-control', 'input_type': 'number'})
        self.fields['cantCreditos'].widget.attrs.update({'class': 'form-control', 'input_type': 'number'})
        
        
    class Meta:
        model = Materia
        fields = ['nombreMateria', 'nombreProfesor', 'semestre','cantCreditos']
        labels = {
            'nombreMateria': 'Nombre de la materia',
            'semestre': 'Semestre',
            'nombreProfesor': 'Nombre del profesor',
            'cantCreditos': 'Cantidad de créditos'
        }
        widgets = {
            'nombreMateria': forms.TextInput(attrs={'class': 'form-control'}),
            'nombreProfesor': forms.TextInput(attrs={'class': 'form-control'}),
            'semestre': forms.NumberInput(attrs={'class': 'form-control'}),
            'cantCreditos': forms.NumberInput(attrs={'class': 'form-control'})
        }
        
class SemestreForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args,**kwargs)
        self.fields['numerosemestre'].widget.attrs.update({'class': 'form-control', 'input_type': 'number'})
        self.fields['creditos'].widget.attrs.update({'class': 'form-control', 'input_type': 'number'})
        self.fields['promedio'].widget.attrs.update({'class': 'form-control', 'input_type': 'number'})
        self.fields['cantMaterias'].widget.attrs.update({'class': 'form-control', 'input_type': 'number'})
        
        
    class Meta:
        model = Semestre
        fields = ['numerosemestre', 'creditos', 'promedio','cantMaterias']
        labels = {
            'numerosemestre': 'Numero del semestre',
            'creditos': 'Creditos totales del semestre',
            'promedio': 'Promedio del semestre',
            'cantMaterias': 'Cantidad de materias del semestre'
        }
        widgets = {
            'numerosemestre': forms.NumberInput(attrs={'class': 'form-control'}),
            'creditos': forms.NumberInput(attrs={'class': 'form-control'}),
            'promedio': forms.NumberInput(attrs={'class': 'form-control'}),
            'cantMaterias': forms.NumberInput(attrs={'class': 'form-control'})
        }