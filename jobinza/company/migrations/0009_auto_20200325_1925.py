# Generated by Django 2.2.11 on 2020-03-25 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0008_auto_20200324_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createpost',
            name='deadline',
            field=models.DateTimeField(blank=True),
        ),
    ]
