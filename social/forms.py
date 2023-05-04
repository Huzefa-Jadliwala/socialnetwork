from django import forms
from .models import Post,Comment, MessageModel

#form used to create new post
class PostForm(forms.ModelForm):
    body = forms.CharField(
        label="",
        widget=forms.Textarea(attrs={
        'rows':'3',
        'placeholder': 'Say Something....',
        })
        )
    image = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(attrs={
        'multiple': True
        })
        
        )
    class Meta:
        model = Post
        fields = ['body']

#form used to create new comment on the post 
class CommentForm(forms.ModelForm):
    comment = forms.CharField(
        label="",
        widget=forms.Textarea(attrs={
        'rows':'3',
        'placeholder': 'Say Something....',
        })
        )
    class Meta:
        model = Comment
        fields = ['comment']

#form used to create new thread between two users so they can start chatting
class ThreadForm(forms.Form):
    username = forms.CharField(label='', max_length=100)

#form used to create new message
class MessageForm(forms.ModelForm):
    body = forms.CharField(label='Message', max_length=1000)
    image = forms.ImageField(required=False)
    class Meta:
        model = MessageModel
        fields = ['body','image']

#form used to search for tags in posts and comments
class ExploreForm(forms.Form):
    query = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={
            'placeholder': 'Explore Tags...',
        })
    )