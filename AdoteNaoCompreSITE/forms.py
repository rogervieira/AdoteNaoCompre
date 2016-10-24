from django.forms import ModelForm, ModelChoiceField
from django.contrib.auth.models import User
from AdoteNaoCompreSITE.models.dog import Dog
from AdoteNaoCompreSITE.models.breed import Breed
from django import forms


class DogForm(ModelForm):
    class Meta:
        model = Dog
        fields = "__all__"
        exclude = ["IdProtetor","Interesse","DataRegistro"]
        breed = ModelChoiceField(queryset= Breed.objects.all(), empty_label='')

        labels = {
             'Info': ('Informações'),
            'IdRaca': ('Raça')
        }


class LoginForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Senha")

    class Meta:
        model = User
        fields = ['username','password']
    
        labels = {
            'username': ('Usuário'),
        }


class SearchDogForm(ModelForm):
    class Meta:
        model = Dog
        fields = ["Sexo", "Idade"]


class UserForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Senha")
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Confirmar senha")

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]

        labels = {
            'username': ('Usuário'),
            'first_name':('Nome'),
            'last_name': ('Sobrenome'),
            'email': ('E-mail'),
        }