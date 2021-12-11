from django import forms
from django.core.exceptions import ValidationError

# validator functions

def username_validator(value):

  print ("validating username")
  # @todo check proper username format
  #raise ValidationError("invalid username format")


# --------

# fields


class UsernameField(forms.CharField):

  def clean(self, value):
    
    clean_data = super().clean(value)
    
    # clean here

    return clean_data




class MyAuthForm(forms.Form):

  username = UsernameField(label='username', max_length=20, validators=[username_validator])
  password = forms.CharField(label='the p', max_length=32, widget=forms.PasswordInput) 