
from tinymce.models import HTMLField
from django.db import models
from django.utils.html import escape, mark_safe
from django.dispatch import receiver
from django.utils import timezone
from djrichtextfield.widgets import RichTextWidget
from djrichtextfield.models import RichTextField
from django.utils.translation import ugettext_lazy 
from django import forms





STATES = (
    ('', 'Choose...'),
    ('MG', 'Minas Gerais'),
    ('SP', 'Sao Paulo'),
    ('RJ', 'Rio de Janeiro')
)


State_CHOICES = (
    ('program1','PROGRAM1', ),
    ('program2', 'PROGRAM2'),
    ('program3','PROGRAM3'),
    ('program4','PROGRAM4'),
    ('program5','PROGRAM5'),
)


class registration(models.Model) :

    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput())
    address_1 = forms.CharField(
        label='Address',
        widget=forms.TextInput(attrs={'placeholder': '1234 Main St'})
    )
    address_2 = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Apartment, studio, or floor'})
    )
    city = forms.CharField()
    state = forms.ChoiceField(choices=STATES)
    zip_code = forms.CharField(label='Zip')
    check_me_out = forms.BooleanField(required=False)

class Post(models.Model):
     
    email = models.EmailField(max_length=70,blank=True, null=True)
    first_name = models.CharField(max_length=70,blank=True, null=True)
    last_name = models.CharField(max_length=70,blank=True, null=True)
    address = models.CharField(max_length=70,blank=True, null=True)
    country= models.CharField(max_length=70,blank=True, null=True)
    zip_code=  models.CharField(max_length=70,blank=True, null=True) 
    city=  models.CharField(max_length=70,blank=True, null=True)
    school=models.CharField(max_length=70,blank=True, null=True)
    phone_number= models.CharField(max_length=70,blank=True,null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    

    def publish(self):
        self.published_date = timezone.now()
        self.save()





