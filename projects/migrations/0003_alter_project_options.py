# Generated by Django 4.1.2 on 2023-05-24 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_task'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-date_created']},
        ),
    ]
