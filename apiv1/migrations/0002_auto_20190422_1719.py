# Generated by Django 2.2 on 2019-04-22 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiv1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leadinteraction',
            name='call_status',
            field=models.IntegerField(blank=True, choices=[(0, 'Call pending'), (1, 'Call answered'), (2, 'Call unanswered'), (6, 'Call rescheduled'), (3, 'Recall pending'), (4, 'Recall answered'), (5, 'Recall unanswered'), (7, 'Recall rescheduled')], null=True),
        ),
        migrations.AlterField(
            model_name='leadinteraction',
            name='meeting_status',
            field=models.IntegerField(blank=True, choices=[(1, 'Meeting pending'), (2, 'Meeting accomplished'), (3, 'Meeting rescheduled'), (4, 'Meeting canceled')], null=True),
        ),
    ]