# Generated by Django 5.1.1 on 2024-10-11 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0012_alter_offre_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offre',
            name='telephone',
            field=models.CharField(max_length=25),
        ),
    ]
