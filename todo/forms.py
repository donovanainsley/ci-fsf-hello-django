from django import forms # type: ignore
from .models import Item


class   ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'done']