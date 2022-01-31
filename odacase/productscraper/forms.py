from django import forms
from .models import PSConfig, PSAttribute


class PSConfigForm(forms.ModelForm):
    class Meta:
        model = PSConfig
        exclude = []
    
    def __init__(self, *args, **kwargs):
        super(PSConfigForm, self).__init__(*args, **kwargs)

class PSAttributeForm(forms.ModelForm):
    class Meta:
        model = PSAttribute
        exclude = ['ps_config',]
