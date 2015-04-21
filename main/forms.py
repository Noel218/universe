#-*- coding:utf-8 -*-

from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator, re
from django.utils.encoding import smart_unicode


def unibot_validator(value):
    if value:
        raise ValidationError('should be empty')

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
    unibot = forms.CharField(validators=[unibot_validator], required=False, widget=forms.HiddenInput())