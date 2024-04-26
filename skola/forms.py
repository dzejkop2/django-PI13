from django import forms
from . models import Uzivatel

class Uzivatel_form(forms.ModelForm):
    
    class Meta:
        model = Uzivatel
        fields = "__all__"