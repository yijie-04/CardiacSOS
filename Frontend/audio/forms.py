# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class audioform(forms.Form):
    
    text = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "text",
                "class": "form-control"
            }
        ))