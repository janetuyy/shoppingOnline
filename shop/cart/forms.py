from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, label = 'Количество', coerce=int, widget=forms.TextInput(attrs={
        'value': 1,
        'max': 20,
        'min': 1,
        'type': 'number',
    }))
    override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

