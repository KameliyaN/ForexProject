from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.forms import HiddenInput
from django.utils.translation import ugettext_lazy as _
from common_app.models import Article, Comment


class ArticleForm(forms.ModelForm):
    use_required_attribute = False
    title = forms.CharField(widget=forms.TextInput())
    content = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = Article
        exclude = ('user',)

    def clean_title(self):
        title = self.cleaned_data.get('title', '')

        if not title[0].isupper():
            raise ValidationError('Title must starts with uppercase letter!')
        return title


class CommentForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = Comment
        exclude = ('user', 'article')
