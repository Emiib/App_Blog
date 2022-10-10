from django import forms
from .models import Post, Comment


class NewPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('anime_name','sub_name','content', 'photo','published_at','category')
        widgets = {'content': forms.Textarea(attrs={'required': True, 'cols': 80}),
                   'photo': forms.FileInput(),
                   'published_at': forms.DateInput(attrs={'type': 'date'})}

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name_person', 'content')


