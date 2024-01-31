import re

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from shoppingapp.models import Login, shopkeeper, User, Schedule


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


def phone_number_validator(value):
    if not re.compile(r'^[7-9]\d{9}$').match(value):
        raise ValidationError('This is Not a Valid Phone Number')


class LoginRegister(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput)

    class Meta:
        model = Login
        fields = ('username', 'password1', 'password2')


class shopkeeperRegister(forms.ModelForm):
    phone_no = forms.CharField(validators=[phone_number_validator])

    class Meta:
        model = shopkeeper
        fields = ('name', 'company_name', 'address', 'phone_no', 'email')


GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female')
)


class UserRegister(forms.ModelForm):
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=GENDER_CHOICES)
    phone_no = forms.CharField(validators=[phone_number_validator])

    class Meta:
        model = User
        fields = ('name', 'age', 'gender', 'address', 'phone_no')


class SchdeuleForm(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    start_time = forms.TimeField(widget=TimeInput, )
    end_time = forms.TimeField(widget=TimeInput, )

    class Meta:
        model = Schedule
        fields = ('shop', 'date', 'start_time', 'end_time')
