from django import forms
from django.core.exceptions import ValidationError

from blog_app.models import Blog, Post, Comment


def check_length(value):
    if len(value) < 10:
        raise ValidationError("Ten post jest za krótki, minimum 50 znaków")


class AddPostForm(forms.Form):
    blog = forms.ModelChoiceField(queryset=Blog.objects.all())
    text = forms.CharField(widget=forms.Textarea())


class AddPostFromBlogForm(forms.Form):
    number = forms.IntegerField()
    text = forms.CharField(widget=forms.Textarea(), validators=[check_length])  # podajemy validator z góry

    def clean(self):  # jeżeli przejdzie przez validatory to będzie działało
        data = super().clean()  # metoda domyślna .clean zwraca słownik data z number i text (bo tak jest zdefiniowana)
        if 'text' not in data:  # jeżeli nie przejdzie przez validator to nie bedzie text w słowniku
            return
        if len(data['text']) < data['number']:
            raise ValidationError('Za krótki tekst')
        return data


class AddPostModelForm(forms.ModelForm):  # automatyczny sposów tworzenia formularzy

    class Meta:
        model = Post  # to jest nasza classa Post
        exclude = ['blog', 'creation.date']  # wyklczamy pola aby dodawane automatycznie sie pojawialy
        # można by fields = [] i wtedy podajemy które pola mają być


class AddCommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['author']
