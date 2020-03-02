from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError
from stories.models import (registration, Post)
from django.forms import ModelChoiceField
from django.forms import ModelMultipleChoiceField
from django.forms import ModelForm
from django.utils.translation import ugettext



class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields =  ('email',  'first_name', 'last_name',  'address', 'city', 'zip_code', 'country', 'school', 'phone_number',)
       