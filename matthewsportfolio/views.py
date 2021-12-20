from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Field, Project, Skill, Message, Endorsement, Person
from .forms import CommentForm, FieldForm, PersonForm, ProjectForm, MessageForm, SkillForm, EndorsementForm


#--------------- HomePage views ---------------#
def HomePage(request):
    persons = Person.objects.all()
    fields = Field.objects.all()
    projects = Project.objects.all()
    detailed_skills = Skill.objects.exclude(description='')
    skills = Skill.objects.filter(description='')
    endorsements = Endorsement.objects.filter(approved=True)
    form = MessageForm()
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message was successfully sent!')
    context = {'persons': persons, 'fields': fields, 'projects': projects, 'detailed_skills': detailed_skills, 'skills': skills, 'endorsements': endorsements, 'form': form}
    return render(request, 'base/home.html', context)


#--------------- Dashboard views ---------------#
def DashboardPage(request):
    unread_count = Message.objects.filter(is_read=False).count()
    context = {'unread_count': unread_count}

    if request.user.is_authenticated:
        return render(request, 'base/dashboard.html', context)
    else:
        return redirect('../admin/')

def FieldManagementPage(request):
    fields = Field.objects.all()

    context = {'fields': fields}
    return render(request, 'base/field_management.html', context)

def ProjectManagementPage(request):
    fields = Field.objects.all()
    projects = Project.objects.all()

    context = {'fields': fields, 'projects': projects}
    return render(request, 'base/project_management.html', context)

def SkillManagementPage(request):
    fields = Field.objects.all()
    detailed_skills = Skill.objects.exclude(description='')
    skills = Skill.objects.filter(description='')

    context = {'fields': fields, 'detailed_skills': detailed_skills, 'skills': skills}
    return render(request, 'base/skill_management.html', context)

#--------------- User Profile views ---------------#
def UserProfilePage(request):
    person = Person.objects.all().last()
    form = PersonForm()
    form_title = 'Personal Profile'

    if request.method == 'POST':
        form = PersonForm(request.POST, request.FILES, instance=person)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {'form': form, 'form_title': form_title}
    return render(request, 'base/form.html', context)
    

#--------------- Field views ---------------#
def FieldPage(request, pk):
    field = Field.objects.get(id=pk)
    form = FieldForm()
    projects = field.project_set.all()
    context = {'field': field, 'form': form, 'projects': projects}
    return render(request, 'base/field.html', context)

def AddField(request):
    form = FieldForm()

    if request.method == 'POST':
        form = FieldForm(request.POST, request.FILES)
        form_title = 'Add Field'
        if form.is_valid():
            form.save()
            return redirect('field-management')

    context = {'form': form, 'form_title': form_title}
    return render(request, 'base/form.html', context)

def DeleteField(request, pk):
    field = Field.objects.get(id=pk)
    field.delete()

    return redirect('field-management')

def EditField(request, pk):
    field = Field.objects.get(id=pk)
    form = FieldForm(instance=field)
    form_title = 'Edit Field'

    if request.method == 'POST':
        form = FieldForm(request.POST, request.FILES, instance=field)
        if form.is_valid():
            form.save()
            return redirect('field-management')

    context = {'form': form, 'form_title': form_title}
    return render(request, 'base/form.html', context)


#--------------- Project views ---------------#
def ProjectPage(request, pk):
    project = Project.objects.get(id=pk)
    count = project.comment_set.count()
    comments = project.comment_set.all().order_by('created')
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.project = project
            comment.save()
            messages.success(request, 'Your comment was successfully sent!')
    context = {'project': project, 'count': count, 'comments': comments, 'form': form}
    return render(request, 'base/project.html', context)

def AddProject(request):
    form = ProjectForm()
    form_title = 'Add Project'

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('project-management')

    context = {'form': form, 'form_title': form_title}
    return render(request, 'base/form.html', context)

def DeleteProject(request, pk):
    project = Project.objects.get(id=pk)
    project.delete()

    return redirect('project-management')

def EditProject(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)
    form_title = 'Edit Project'

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project-management')

    context = {'form': form, 'form_title': form_title}
    return render(request, 'base/form.html', context)



#--------------- Skill views ---------------#
def AddSkill(request):
    form = SkillForm()
    form_title = 'Add Skill'
    if request.method == 'POST':
        form = SkillForm(request.POST, request.FILES)
        form.save()
        messages.success(request, 'Your skill was successfully added!')
        return redirect('skill-management')
    context = {'form': form, 'form_title': form_title}
    return render(request, 'base/form.html', context)

def DeleteSkill(request, pk):
    skill = Skill.objects.get(id=pk)
    skill.delete()

    return redirect('skill-management')

def EditSkill(request, pk):
    skill = Skill.objects.get(id=pk)
    form = SkillForm(instance=skill)
    form_title = 'Edit Skill'

    if request.method == 'POST':
        form = FieldForm(request.POST, request.FILES, instance=skill)
        if form.is_valid():
            form.save()
            return redirect('skill-management')

    context = {'form': form, 'form_title': form_title}
    return render(request, 'base/form.html', context)


#--------------- Inbox views ---------------#
def InboxPage(request):
    inbox = Message.objects.all().order_by('is_read')
    unread_count = Message.objects.filter(is_read=False).count()
    context = {'inbox': inbox, 'unread_count': unread_count}
    return render(request, 'base/inbox.html', context)

#--------------- Message views ---------------#
def MessagePage(request, pk):
    message = Message.objects.get(id=pk)
    message.is_read = True
    message.save()
    context = {'message': message}
    return render(request, 'base/message.html', context)


#--------------- Endorsement views ---------------#
def AddEndorsement(request):
    form = EndorsementForm()
    form_title = 'Add Endorsement'
    if request.method == 'POST':
        form = EndorsementForm(request.POST)
        form.save()
        messages.success(request, 'Your Endorsement was successfully added!')
        return redirect('home')
    context = {'form': form, 'form_title': form_title}
    return render(request, 'base/form.html', context)


#--------------- Donation views ---------------#
def DonationPage(request):
    return render(request, 'base/donation.html')