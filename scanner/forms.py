# -*- coding: utf-8 -*-
from django import forms
from settings import *

class MoviePathForm(forms.Form):
    path = forms.CharField(max_length = 1000, help_text = 'The local directory where the movie files are stored')
    

