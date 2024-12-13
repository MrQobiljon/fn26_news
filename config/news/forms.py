from django import forms

from .models import Category, Post


class PostForm(forms.Form):
    name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={
        "placeholder": "Maqola nomi",
        'class': "form-control"
    }))
    content = forms.CharField(required=False, widget=forms.Textarea(attrs={
        "placeholder": "Maqola matni",
        'class': "form-control",
        "rows": 3
    }))
    photo = forms.ImageField(required=False, widget=forms.FileInput())
    category = forms.ModelChoiceField(queryset=Category.objects.all(),
                                      widget=forms.Select(attrs={
                                          "class": "form-select"
                                      }))
    published = forms.BooleanField(widget=forms.CheckboxInput(attrs={
        "class": "form-check-input",
        "checked": "checked"
    }))
    video = forms.FileField(required=False, widget=forms.FileInput())

    def create(self):
        post = Post.objects.create(**self.cleaned_data)
        return post