from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control", "placeholder": "Nome de utilizador"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "E-mail"}),
            "password1": forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Palavra-passe"}),
            "password2": forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Palavra-passe"}),
        }

        labels = {
            "username": "Nome de utilizador",
            "email": "E-mail",
            "password1": "Palavra-passe",
            "password2": "Confirmar palavra-passe",
        }

        help_texts = {
            "username": "Insira o nome com que pretende ser identificado.",
            "email": "Insira o seu e-mail.",
            "password1": "Insira uma palavra-passe com pelo menos 8 caracteres alfanuméricos.",
            "password2": "Confirme a palavra-passe inserida anteriormente.",
        }

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
