# Generated by Django 2.2.11 on 2020-03-25 21:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_auto_20200323_2152'),
    ]

    operations = [
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
