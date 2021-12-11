from django import forms
from django.core.exceptions import ValidationError
from ..models import BlogArticle

from datetime import datetime


CreateBlogForm = forms.modelform_factory( BlogArticle, exclude=['publish_date'] )



"""
forms.DateTimeField has to be subclassed in order to manipulate the separate date and time input
"""
class CustomDateTimeField(forms.DateTimeField):

  def clean(self, value):
    
    # bypass
    # @todo validate the format of the values
    # should be a list of two values , one is date and other is time
    clean_data = value #super().clean(value)

    return clean_data


class CustomCreateBlogForm(CreateBlogForm):

    the_d = CustomDateTimeField(widget=forms.SplitDateTimeWidget(date_attrs={'type':'date'}, time_attrs={'type':'time'}) ) 
    
    def __init__(self, *args, **kwargs):

      # prepare any thing that needs to be loaded
      if kwargs.get('instance', None):
        kwargs['initial'] = { 'the_d' :  kwargs['instance'].publish_date }

      super().__init__(*args, **kwargs)

    def clean(self):

      cleaned_data = super().clean()
      datetime_value = cleaned_data.get('the_d', None)
      datetime_value_formatted = '%s %s' % (datetime_value[0], datetime_value[1]) 

      self.instance.publish_date = datetime_value_formatted