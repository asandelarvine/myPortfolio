# Generated by Django 3.2.9 on 2022-03-03 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioapp', '0004_project_proj_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='experience',
            name='responsibilities_3',
        ),
        migrations.RemoveField(
            model_name='experience',
            name='responsibilities_4',
        ),
    ]