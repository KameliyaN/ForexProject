from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.utils.translation import ugettext_lazy as _
from common_app.models import Article, Comment


class ArticleForm(forms.ModelForm):
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

    # def clean_content(self):
    #     content = self.cleaned_data['content']
    #     if not content:
    #         raise ValidationError('This field is required')
    #     return content


class CommentForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = Comment
        exclude = ('user', 'article')
