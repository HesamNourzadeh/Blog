from django import forms
from django.contrib.auth.models import User
from django.core.validators import ValidationError
from .models import Message
class ContactUsForm(forms.Form):
    BIRTH_YEAR_CHOICES = [i for i in range(1980 , 2000+1)]
    name = forms.CharField(max_length=10 , label = 'your name:' )
    text = forms.CharField(max_length=10 , label = 'your text')
    birth = forms.DateField(widget = forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))

    def clean(self):
        name = self.cleaned_data.get('name')
        text = self.cleaned_data.get('text')
        if name == text:
            raise ValidationError('!!!---name == text---!!!' , code=1)
class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'
        widgets = {
            "title" : forms.TextInput(attrs={
                'class' : 'form-control form-control-lg',
                'max-width' : '700px',
                'placeholder' : 'enter your title'
            }),
            "text" : forms.Textarea(attrs={
                'class': 'form-control form-control-lg',
                'max-width': '700px',
                'placeholder': 'enter your text'
            }),
          "email" : forms.TextInput(attrs={
              'class': 'form-control form-control-lg',
              'max-width': '700px',
              'placeholder': 'enter your email'
          })
        }


