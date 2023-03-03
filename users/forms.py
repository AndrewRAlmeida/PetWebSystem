from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from users.models import Usuario


# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = Usuario
		fields = ("nome", "bairro", "email", "password1", "password2")

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
		user = authenticate(username=dados['email'], password=dados['password'])
		# if user is None:
		# 	raise forms.ValidationError('Verifique os dados e tente novamente')
		return dados