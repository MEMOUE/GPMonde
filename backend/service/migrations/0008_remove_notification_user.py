# Generated by Django 5.1.1 on 2024-10-06 21:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0007_notification_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='user',
        ),
    ]
