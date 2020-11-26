from django import forms

from currencies.models import Currency, Category, Links


class CurrencyForm(forms.ModelForm):
    current_interest_rate = forms.URLField(widget=forms.URLInput())
    currency_history = forms.CharField(widget=forms.Textarea())
    picture = forms.ImageField(required=False)

    class Meta:
        model = Currency
        fields = '__all__'


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class LinksForm(forms.ModelForm):
    class Meta:
        model = Links
        fields = '__all__'
