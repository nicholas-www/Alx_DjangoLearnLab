from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]




class PostForm(forms.ModelForm):
    tags = forms.CharField(required=False, help_text="Separate tags with commas")

    class Meta:
        model = Post
        fields = ["title", "content", "tags"]

    def save(self, commit=True, *args, **kwargs):
        instance = super().save(commit=False, *args, **kwargs)
        if commit:
            instance.save()
            # Save tags
            tag_names = [t.strip() for t in self.cleaned_data["tags"].split(",") if t.strip()]
            tag_objs = []
            for name in tag_names:
                tag_obj, created = Tag.objects.get_or_create(name=name)
                tag_objs.append(tag_obj)
            instance.tags.set(tag_objs)
        return instance


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]