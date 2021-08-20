from django import forms
from django.forms import ModelForm
from .models import Contact, Post, Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



# from django.db import transaction
# class AdminSignUpForm(UserCreationForm):
# phone_number = forms.CharField(required=True)/
#     

#     class Meta(UserCreationForm.Meta):
#         model = User
    
#     @transaction.atomic
#     def save(self):
#         user = super().save(commit=True)
#         user.is_admin = True
#         user.phone_number = self.cleaned_data.get('phone_number')
#         user.save()
#         admin = Admin.objects.create(user=user)
#         admin.phone_number=self.cleaned_data.get('phone_number')
#         admin.save()
#         return user

# class managerSignUpForm(UserCreationForm):

#     phone_number = forms.CharField(required=True)

#     class Meta(UserCreationForm.Meta):
#         model = User

#     @transaction.atomic
#     def save(self):
#         user = super().save(commit=False)
#         user.is_manager = True
#         user.is_staff = True
#         user.first_name = self.cleaned_data.get('first_name')
#         user.last_name = self.cleaned_data.get('last_name')
#         user.save()
#         employee = Employee.objects.create(user=user)
#         employee.phone_number=self.cleaned_data.get('phone_number')
#         employee.designation=self.cleaned_data.get('designation')
#         employee.save()
#         return user

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



