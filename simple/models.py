from django.db import models
from django.db.models.fields import SlugField
# Create your models here.


# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     first_name = models.CharField(max_length=30, blank=True)
#     bio = models.CharField(max_length=300, blank=True)

# @receiver(post_save, sender=User)
# def update_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#     instance.profile.save()

# class Manager(models.Model):
#     first_name = models.CharField(max_length=30, blank=True)
#     last_name = models.CharField(max_length=30, blank=True)
#     email = models.EmailField(blank=False, max_length=254)

#     def __str__(self):
#         return self.first_name

#     def save_manager(self):
#         self.save()

#     def delete_manager(self):
#         self.delete()
class Contact(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=225)
    message = models.TextField()

    def __str__(self):
        return self.email


class Post (models.Model):
    title = models.TextField(max_length=50)
    description = models.TextField(max_length=225)
    image = models.ImageField(upload_to ='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_added']