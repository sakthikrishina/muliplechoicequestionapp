# Generated by Django 4.2.11 on 2024-04-26 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Institution', '0014_performanceplot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='performanceplot',
            name='plot_image',
            field=models.ImageField(upload_to='performance_plots'),
        ),
    ]