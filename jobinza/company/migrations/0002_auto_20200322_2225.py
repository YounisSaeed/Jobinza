# Generated by Django 2.2.11 on 2020-03-22 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='createpost',
            name='related_industry',
        ),
        migrations.RemoveField(
            model_name='createpost',
            name='rolejob',
        ),
        migrations.AlterField(
            model_name='createpost',
            name='skills',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.DeleteModel(
            name='jobRole',
        ),
        migrations.DeleteModel(
            name='relatedIndustry',
        ),
        migrations.DeleteModel(
            name='skills',
        ),
    ]
