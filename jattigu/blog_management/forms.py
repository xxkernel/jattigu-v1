from django import forms
from .models import BlogPost

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'category'] #'tags', 'is_published']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your post content here'}),
            'category': forms.Select(attrs={'class': 'form-control', 'empty_label': 'No Category'}),
            # 'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),
            # 'is_published': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
