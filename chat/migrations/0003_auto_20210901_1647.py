# Generated by Django 3.1.5 on 2021-09-01 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_auto_20210831_0910'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='record',
            new_name='content_or_record',
        ),
        migrations.RemoveField(
            model_name='message',
            name='content',
        ),
    ]