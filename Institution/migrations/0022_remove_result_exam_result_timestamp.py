# Generated by Django 4.2.11 on 2024-05-09 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Institution', '0021_remove_question_current_question_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='exam',
        ),
        migrations.AddField(
            model_name='result',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
