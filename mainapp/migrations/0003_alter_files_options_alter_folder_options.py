# Generated by Django 4.1.1 on 2022-12-07 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_folder_password_folder_private'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='files',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterModelOptions(
            name='folder',
            options={'ordering': ['-created_at']},
        ),
    ]