# Generated by Django 2.2 on 2019-04-23 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiv1', '0003_auto_20190423_2004'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='meeting_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='lead',
            name='recall_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
