# Generated by Django 4.1.1 on 2022-12-07 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='folder',
            name='password',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='folder',
            name='private',
            field=models.BooleanField(default=False),
        ),
    ]