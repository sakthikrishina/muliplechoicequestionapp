# Generated by Django 4.2.11 on 2024-04-19 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0033_alter_customuser_user_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='father_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='gender',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
