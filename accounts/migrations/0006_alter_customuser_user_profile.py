# Generated by Django 4.2.11 on 2024-04-14 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_remove_customuser_user_proile_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_profile',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pic/%Y/%m/%d'),
        ),
    ]
