# Generated by Django 4.2.11 on 2024-04-17 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Institution', '0002_course_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='status',
            field=models.CharField(choices=[('completed', 'Completed'), ('executed', 'Executed')], max_length=50, null=True),
        ),
    ]
