from django import forms
from .models import Item, Contact


class AddContact(forms.ModelForm):

    class Meta:
        model = Contact
        fields = '__all__'


class AddItem(forms.ModelForm):

    class Meta:
        model = Item
        fields = '__all__'
