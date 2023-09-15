from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from contact.models import Contact


class ContactForm(forms.ModelForm):
    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*',
            }
        )
    )

    class Meta:
        model = Contact
        fields = (
            'first_name', 'last_name', 'phone',
            'email', 'description', 'category',
            'picture',
        )

    def clean(self):
        clean_data = self.cleaned_data
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')

        if first_name == last_name:
            msg = forms.ValidationError('Primeiro nome não pode ser igual ao segundo', code='invalid')
            self.add_error('first_name',msg)
            self.add_error('last_name',msg)

        return super().clean() 
    
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        print(first_name)
        if first_name == 'ABC':
            self.add_error('first_name',
                           forms.ValidationError(
                               'Não Escreva ABC', code='invalid'
                               ))
        return first_name
    

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        required=True,
        min_length=3,
    )
    last_name = forms.CharField(
        required=True,
        min_length=3,
    )
    email = forms.EmailField(
        required=True,
        min_length=3,
    )
    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email',
            'username', 'password1', 'password2',
        )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            self.add_error(
                'email',
                forms.ValidationError('Email ja Cadastrado!', code='invalid')
            )
        return email