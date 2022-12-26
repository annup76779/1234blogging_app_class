from django import forms
from .models import Blogs


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Blogs
        fields = ["title", "image", "video", "category", "content"]

        # HTML input type
        # 1. text       TextInput
        # 2. file       FileInput
        # 3. select     Select
        # 4. textarea   Textarea

        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter blog title"
                }
            ),
            "image": forms.FileInput(attrs={
                "class": "form-control",
            }),
            "video": forms.FileInput(attrs={
                "class": "form-control",
                "required": False
            }),
            "category": forms.Select(attrs={
                "class": "form-control",
            }),
            "content": forms.Textarea(attrs={
                "class": "form-control",
                "id": "blog_body",
                "hidden": "true"
            }),
        }

        labels = {
            "title": "Blog Title",
            "content": ""
        }