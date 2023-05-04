from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.

class Post(models.Model):
    body = models.TextField()
    image = models.ManyToManyField('Image',blank=True)
    created_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, blank=True, related_name='likes')
    dislikes = models.ManyToManyField(User, blank=True, related_name='dislikes')
    tags = models.ManyToManyField('Tag', blank=True)

    # function to generate all the tags present in the post body
    def create_tags(self):
        for word in self.body.split():
            if word[0] == "#":
                tag = Tag.objects.filter(name=word[0]).first()
                if tag:
                    self.tags.add(tag.pk)
                else:
                    tag = Tag(name=word[1:])
                    tag.save()
                    self.tags.add(tag.pk)
                self.save()

    def __str__(self):
        return str(self.body) + ": created by " + str(self.author)
    
class Comment(models.Model):
    comment = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, blank=True, related_name='comments_likes')
    dislikes = models.ManyToManyField(User, blank=True, related_name='comments_dislikes')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='+')
    tags = models.ManyToManyField('Tag', blank=True)

    # function to generate all the tags present in the comment body
    def create_tags(self):
        for word in self.comment.split():
            if word[0] == "#":
                tag = Tag.objects.filter(name=word[0]).first()
                if tag:
                    self.tags.add(tag.pk)
                else:
                    tag = Tag(name=word[1:])
                    tag.save()
                    self.tags.add(tag.pk)
                self.save()

    # function to get all the children comments of the comment
    @property
    def children(self):
        return Comment.objects.filter(parent=self).order_by('-created_on').all()

    # function to check if the parent of the comment exists or not
    @property
    def is_parent(self):
        if self.parent is None:
            return True
        return False

    def __str__(self):
        return str(self.comment) + ": created by " + str(self.author)
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True, verbose_name='user', related_name='profile', on_delete=models.CASCADE)
    name = models.CharField(max_length=30, blank=True, null=True)
    bio = models.CharField(max_length=500, blank=True, null=True)
    birthdate = models.DateTimeField(null=True, blank=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    picture = models.ImageField(upload_to='uploads/profile_pictures', default='uploads/profile_pictures/default.png', blank=True)
    followers = models.ManyToManyField(User, blank=True, related_name="followers")
    

@receiver(signal=post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(signal=post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Notification(models.Model):
    notification_type = models.IntegerField()
    to_user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name='notification_on')
    from_user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name='notification_from')
    post = models.ForeignKey('Post', blank=True, null=True, on_delete=models.CASCADE, related_name="+")
    comment = models.ForeignKey('Comment', blank=True, null=True, on_delete=models.CASCADE, related_name="+")
    thread = models.ForeignKey('ThreadModel', blank=True, null=True, on_delete=models.CASCADE, related_name="+")
    date = models.DateTimeField(default=timezone.now)
    user_has_seen = models.BooleanField(default=False)


class ThreadModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='+')
    reciever = models.ForeignKey(User, on_delete=models.CASCADE,related_name='+')

class MessageModel(models.Model):
    thread = models.ForeignKey('ThreadModel', on_delete=models.CASCADE, related_name='+', null=True, blank=True)
    sender_user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='+')
    reciever_user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='+')
    body = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='uploads/messages',blank=True, null=True)
    date = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=False)

class Image(models.Model):
    image = models.ImageField(upload_to='uploads/post_photos',blank=True, null=True)

class Tag(models.Model):
    name = models.CharField(max_length=255)