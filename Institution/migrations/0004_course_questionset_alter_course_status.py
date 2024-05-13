# Generated by Django 4.2.11 on 2024-04-17 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Institution', '0003_alter_course_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='questionset',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='status',
            field=models.CharField(choices=[('completed', 'Completed'), ('executed', 'Executed'), ('pending', 'Pending')], max_length=50, null=True),
        ),
    ]