from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'old_price', 'discount', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'box', 'placeholder': 'Product Name'}),
            'price': forms.NumberInput(attrs={'class': 'box', 'placeholder': 'Price'}),
            'old_price': forms.NumberInput(attrs={'class': 'box', 'placeholder': 'Old Price'}),
            'discount': forms.TextInput(attrs={'class': 'box', 'placeholder': 'Discount (e.g. -10%)'}),
            'image': forms.FileInput(attrs={'class': 'box'}),
        }
