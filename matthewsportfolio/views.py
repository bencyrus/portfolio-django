from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Project, Skill, Tag, Message, Endorsement, Person
from .forms import CommentForm, ProjectForm, MessageForm, SkillForm, EndorsementForm



def HomePage(request):
    persons = Person.objects.all()
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
    context = {'persons': persons, 'projects': projects, 'detailed_skills': detailed_skills, 'skills': skills, 'endorsements': endorsements, 'form': form}
    return render(request, 'base/home.html', context)

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

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/project_form.html', context)

def EditProject(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/project_form.html', context)

def InboxPage(request):
    inbox = Message.objects.all().order_by('is_read')
    unread_count = Message.objects.filter(is_read=False).count()
    context = {'inbox': inbox, 'unread_count': unread_count}
    return render(request, 'base/inbox.html', context)

def MessagePage(request, pk):
    message = Message.objects.get(id=pk)
    message.is_read = True
    message.save()
    context = {'message': message}
    return render(request, 'base/message.html', context)

def AddSkill(request):
    form = SkillForm()
    if request.method == 'POST':
        form = SkillForm(request.POST, request.FILES)
        form.save()
        messages.success(request, 'Your skill was successfully added!')
        return redirect('home')
    context = {'form': form}
    return render(request, 'base/skill_form.html', context)


def AddEndorsement(request):
    form = EndorsementForm()
    if request.method == 'POST':
        form = EndorsementForm(request.POST)
        form.save()
        messages.success(request, 'Your Endorsement was successfully added!')
        return redirect('home')
    context = {'form': form}
    return render(request, 'base/endorsement_form.html', context)

def DonationPage(request):
    return render(request, 'base/donation.html')