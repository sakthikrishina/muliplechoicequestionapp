# Generated by Django 4.2.11 on 2024-04-25 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Institution', '0012_result_timetaken'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='timetaken',
        ),
        migrations.AddField(
            model_name='result',
            name='duration',
            field=models.IntegerField(help_text='duration of the exam in minutes', null=True),
        ),
    ]
