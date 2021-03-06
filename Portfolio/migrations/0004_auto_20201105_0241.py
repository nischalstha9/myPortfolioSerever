# Generated by Django 3.0.7 on 2020-11-05 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolio', '0003_auto_20201105_0229'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='education',
            options={'ordering': ['-to_date'], 'verbose_name': 'Education', 'verbose_name_plural': 'Educations'},
        ),
        migrations.AlterField(
            model_name='project',
            name='short_desc',
            field=models.TextField(blank=True, null=True, verbose_name='Short Description'),
        ),
        migrations.AlterField(
            model_name='project',
            name='short_info',
            field=models.TextField(blank=True, null=True, verbose_name='Short Info'),
        ),
    ]
