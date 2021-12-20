from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage, name="home"),

    path('dashboard/', views.DashboardPage, name="dashboard"),
    path('edit-profile', views.UserProfilePage, name="edit-profile"),
    path('field-management/', views.FieldManagementPage, name="field-management"),
    path('project-management/', views.ProjectManagementPage, name="project-management"),
    path('skill-management/', views.SkillManagementPage, name="skill-management"),

    path('field/<str:pk>/', views.FieldPage, name="field"),
    path('add-field', views.AddField, name="add-field"),
    path('edit-field/<str:pk>/', views.EditField, name="edit-field"),
    path('delete-field/<str:pk>/', views.EditSkill, name="delete-field"),

    path('project/<str:pk>/', views.ProjectPage, name="project"),
    path('add-project', views.AddProject, name="add-project"),
    path('delete-project/<str:pk>/', views.DeleteProject, name="delete-project"),
    path('edit-project/<str:pk>/', views.EditProject, name="edit-project"),

    path('add-skill', views.AddSkill, name="add-skill"),
    path('delete-skill/<str:pk>/', views.DeleteSkill, name="delete-skill"),
    path('edit-skill/<str:pk>/', views.EditSkill, name="edit-skill"),

    path('inbox/', views.InboxPage, name='inbox'),
    path('message/<str:pk>/', views.MessagePage, name='message'),

    path('add-endorsement', views.AddEndorsement, name="add-endorsement"),


    path('donation/', views.DonationPage, name="donation"),
]