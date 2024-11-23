from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import CustomUser, Orders
from datetime import date, datetime


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Обязательное поле. Введите действующий email.')

    class Meta:
        model = CustomUser
        fields = ('username', 'last_name', 'first_name', 'patronymic', 'email', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['username', 'password']


class NewOrderForm(forms.ModelForm):
    orderdatetime = forms.DateTimeField(label='Дата и время', input_formats='%Y-%m-%d %H:%M:%S', initial=datetime.now(),
                                        widget=forms.DateTimeInput(attrs={'type':'datetime-local'}))


    class Meta:
        model = Orders
        fields = ['phone',
                  'orderdatetime','description']
