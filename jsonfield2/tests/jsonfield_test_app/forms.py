from django import forms

from jsonfield2.forms import JSONFormField
from .models import JSONFieldTestModel


class JSONTestForm(forms.Form):
    json_data = JSONFormField()
    optional_json_data = JSONFormField(required=False)


class JSONTestModelForm(forms.ModelForm):
    
    class Meta:
        model = JSONFieldTestModel
        fields = [ 'json' ]
