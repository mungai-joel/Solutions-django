from django import forms
from django.forms import ModelForm
from .models import Contact, Post, Comment
import django
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models.fields import EmailField
from django import forms

class createuser(UserCreationForm):
    email=forms.EmailField(max_length=200)
    
    class meta:
        model = User
        field = ["username", "email" , "password1" , "password2"]


class ContactForm(ModelForm):

    
    class Meta:
        model = Contact
        fields = '__all__'

class PostForm(ModelForm):

    
    class Meta:
        model = Post
        fields = ['title','description','image']

        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body'] 

# class ProfileForm(forms.ModelForm):
#     last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
#     email = forms.EmailField(required=True)

#     class meta:
#         model = Profile
#         field = ("last_name", "email")
#         exclude = ['prof_user']



