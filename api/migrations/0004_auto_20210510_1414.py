# Generated by Django 3.2.2 on 2021-05-10 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_post_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='description',
        ),
        migrations.RemoveField(
            model_name='group',
            name='slug',
        ),
    ]
