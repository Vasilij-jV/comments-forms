from django import forms
from .models import Comment, CommentForArticle
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')


class ContactForm(forms.Form):
    name = forms.CharField(label='Ваше имя', max_length=100)
    email = forms.EmailField(label='Электронная почта')
    message = forms.CharField(label='Сообщение', widget=forms.Textarea)


class ContactFormToAdmin(forms.Form):
    name = forms.CharField(label='Ваше имя', max_length=100)
    email = forms.EmailField(label='Электронная почта')
    message = forms.CharField(label='Сообщение', widget=forms.Textarea)


class CommentForForm(forms.ModelForm):
    class Meta:
        model = CommentForArticle
        fields = ('name', 'email', 'content')


class UserProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']
