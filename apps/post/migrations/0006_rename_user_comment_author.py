# Generated by Django 3.2.8 on 2024-04-16 18:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='user',
            new_name='author',
        ),
    ]
