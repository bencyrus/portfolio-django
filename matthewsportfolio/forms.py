from django.db import models
from django.db.models import fields
from django.forms import ModelForm
from .models import Endorsement, Field, Project, Message, Skill, Comment, Person


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PersonForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['last_name'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['headline'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['description'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['about'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['more_about'].widget.attrs.update(
            {'class': 'form-control'})

class FieldForm(ModelForm):
    class Meta:
        model = Field
        fields = ['title', 'logo', 'description']

    def __init__(self, *args, **kwargs):
        super(FieldForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update(
            {'class': 'form-control'})

        self.fields['description'].widget.attrs.update(
            {'class': 'form-control'})

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'thumbnail', 'field', 'description']

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update(
            {'class': 'form-control'})

        self.fields['description'].widget.attrs.update(
            {'class': 'form-control'})

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = '__all__'
        exclude = ['is_read']

    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {'class': 'form-control'})

        self.fields['email'].widget.attrs.update(
            {'class': 'form-control'})

        self.fields['subject'].widget.attrs.update(
            {'class': 'form-control'})

        self.fields['content'].widget.attrs.update(
            {'class': 'form-control'})

class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = '__all__'
        exclude = ['id', 'created']

    def __init__(self, *args, **kwargs):
        super(SkillForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update(
            {'class': 'form-control'})

        self.fields['description'].widget.attrs.update(
            {'class': 'form-control'})

class EndorsementForm(ModelForm):
    class Meta:
        model = Endorsement
        fields = '__all__'
        exclude = ['featured', 'approved']

    def __init__(self, *args, **kwargs):
        super(EndorsementForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {'class': 'form-control'})

        self.fields['content'].widget.attrs.update(
            {'class': 'form-control'})

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        exclude = ['project', 'created']

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {'class': 'form-control'})

        self.fields['comment'].widget.attrs.update(
            {'class': 'form-control'})
