from django import forms


class OrderForm(forms.Form):
    name = forms.CharField(max_length=200, required=False)
    email = forms.CharField(max_length=200)