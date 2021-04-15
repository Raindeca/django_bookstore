from django import forms
from .models import Invoice


class InvoiceForm(forms.ModelForm):

    class Meta:
        model = Invoice
        fields = ['user', 'item', 'invoice_date' ,'payment_method', 'item', 'total']