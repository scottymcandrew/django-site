from django import forms


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    to = forms.EmailField()
    # Widget determines how the field is rendered in HTML. Default is <input type="text">
    # Textarea widget changes HTML to <textarea> element instead
    comments = forms.CharField(required=False, widget=forms.Textarea)
