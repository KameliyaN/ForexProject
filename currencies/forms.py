from django import forms

from currencies.models import Currency


class CurrencyForm(forms.ModelForm):
    current_interest_rate = forms.URLField(widget=forms.URLInput())
    currency_history = forms.CharField(widget=forms.Textarea())
    picture = forms.ImageField(required=False)

    class Meta:
        model = Currency
        fields = '__all__'
