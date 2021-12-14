# Generated by Django 4.0 on 2021-12-14 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matthewsportfolio', '0010_field_project_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='name',
        ),
        migrations.AddField(
            model_name='person',
            name='first_name',
            field=models.CharField(default='Matthew', max_length=255),
        ),
        migrations.AddField(
            model_name='person',
            name='last_name',
            field=models.CharField(default='Mohaghegh', max_length=255),
        ),
    ]