# Generated by Django 3.0.7 on 2020-11-05 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolio', '0004_auto_20201105_0241'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-id'], 'verbose_name': 'Project', 'verbose_name_plural': 'Projects'},
        ),
        migrations.AddField(
            model_name='project',
            name='remarks',
            field=models.TextField(blank=True, null=True, verbose_name='Short Description'),
        ),
        migrations.AlterField(
            model_name='experience',
            name='to_date',
            field=models.DateField(verbose_name='To Date'),
        ),
    ]