from django.contrib import admin

from .models import Person, Project, Skill, Tag, Message, Endorsement, Comment
admin.site.register(Person)
admin.site.register(Project)
admin.site.register(Comment)
admin.site.register(Skill)
admin.site.register(Tag)
admin.site.register(Message)
admin.site.register(Endorsement)