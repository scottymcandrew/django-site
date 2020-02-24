from django import forms
from .models import Comment


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    to = forms.EmailField()
    # Widget determines how the field is rendered in HTML. Default is <input type="text">
    # Textarea widget changes HTML to <textarea> element instead
    comments = forms.CharField(required=False, widget=forms.Textarea)


class CommentForm(forms.ModelForm):  # ModelForm builds the form dynamically based on the Comment model
    class Meta:
        # Here we specify the model (Comment) to build the form
        model = Comment
        # Django builds the form based on all model fields by default. Use fields to limit this
        fields = ('name', 'email', 'body')
