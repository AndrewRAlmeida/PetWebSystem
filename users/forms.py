from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse_lazy

from users.models import Usuario

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = Usuario
		fields = ("nome", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class LoginForm(forms.ModelForm):
	class Meta:
		model = Usuario
		fields = ("email", "password",)

	password = forms.CharField(widget=forms.PasswordInput, label="senha")

	def clean(self):
		dados = self.cleaned_data
		return dados

class MinhaContaForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('email', 'nome', 'cpf', 'telefone')

    senha = forms.CharField(
        label='Senha',
        # help_text='<a href="{link}">(clique aqui para alterar a sua senha)</a>'.format(link=reverse_lazy('mudar_senha')),
        widget=forms.PasswordInput(attrs={'readonly':'readonly'}),
        required=False
    )

    def __init__(self, *args, **kwargs):
        super(MinhaContaForm, self).__init__(*args, **kwargs)

        for fieldname in ['email']:
            self.fields[fieldname].help_text = None