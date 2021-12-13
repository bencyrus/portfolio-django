from django.db import models
from django.core.exceptions import ValidationError
import uuid
from ckeditor_uploader.fields import RichTextUploadingField


class Person(models.Model):
    name = models.CharField(max_length=255, default='Matthew Mohaghegh')
    profile_picture = models.ImageField(null=True, default='static/images/profile.png')
    headline = models.CharField(max_length=255, default='portfolio Manager')
    description = models.CharField(max_length=400, default="I do a lot of crazy stuff with people's money!")
    about = models.CharField(max_length=2000, null=True, blank=True, default='Lorem ipsum, dolor sit amet consectetur adipisicing elit. \
        Officiis porro itaque ipsum distinctio, inventore consequuntur nisi quis tenetur blanditiis illum quod voluptates.\
        Sit odit dolorum aperiam, deserunt veniam quia aut? Lorem ipsum dolor sit amet consectetur adipisicing elit. Corrupti \
        alias, exercitationem atque obcaecati accusantium necessitatibus impedit delectus sequi?')

    def clean(self):
        if Person.objects.exists() and not self.pk:
            raise ValidationError('only one user is allowed')

    def __str__(self):
        return self.name

class Project(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    title = models.CharField(max_length=255) 
    thumbnail = models.ImageField(null=True)
    description = RichTextUploadingField()
    slug = models.SlugField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[0:50]

class Skill(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    logo = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Tag(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Message(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    content = models.TextField()
    is_read = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Endorsement(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField()
    approved = models.BooleanField(default=False, null = True)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.content[0:50]