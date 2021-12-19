from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage, name="home"),

    path('field/<str:pk>/', views.FieldPage, name="field"),
    path('add-field', views.AddField, name="add-field"),
    path('edit-field/<str:pk>/', views.EditField, name="edit-field"),

    path('project/<str:pk>/', views.ProjectPage, name="project"),
    path('add-project', views.AddProject, name="add-project"),
    path('edit-project/<str:pk>/', views.EditProject, name="edit-project"),

    path('inbox/', views.InboxPage, name='inbox'),
    path('message/<str:pk>/', views.MessagePage, name='message'),

    path('add-skill', views.AddSkill, name="add-skill"),
    path('add-endorsement', views.AddEndorsement, name="add-endorsement"),

    path('dashboard/', views.DashboardPage, name="dashboard"),

    path('donation/', views.DonationPage, name="donation"),
]