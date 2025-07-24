from django import forms

class ExampleForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your name'}),
        required=True
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'}),
        required=True
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Your message'}),
        required=True
    )