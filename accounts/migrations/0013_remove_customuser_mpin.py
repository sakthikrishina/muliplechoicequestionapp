# Generated by Django 4.2.11 on 2024-04-14 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_alter_customuser_user_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='mpin',
        ),
    ]
