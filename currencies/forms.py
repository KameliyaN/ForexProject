from django import forms
from django.core.exceptions import ValidationError

from django.core.validators import URLValidator
from currencies.models import Currency, Category, Links


class CurrencyForm(forms.ModelForm):
    use_required_attribute = False

    name = forms.CharField(widget=forms.TextInput())
    current_interest_rate = forms.URLField(widget=forms.URLInput())
    currency_history = forms.CharField(widget=forms.Textarea())
    picture = forms.ImageField(required=False)

    class Meta:
        model = Currency
        fields = '__all__'


class CategoryForm(forms.ModelForm):
    use_required_attribute = False

    class Meta:
        model = Category
        fields = '__all__'


class LinksForm(forms.ModelForm):
    use_required_attribute = False

    class Meta:
        model = Links
        fields = '__all__'
