from django import forms
from .models import Order, OrderItem

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'


OrderItemFormSet = forms.inlineformset_factory(Order, OrderItem, fields=('__all__',), extra=1)

