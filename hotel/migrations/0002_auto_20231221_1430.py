# Generated by Django 3.1.4 on 2023-12-21 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactmessage',
            name='subject',
        ),
        migrations.AddField(
            model_name='contactmessage',
            name='phone_number',
            field=models.CharField(default='', max_length=15),
        ),
    ]
