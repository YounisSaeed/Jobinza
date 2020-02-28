# Generated by Django 2.2.10 on 2020-02-26 16:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='createpost',
            name='deadline',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 2, 26, 16, 19, 11, 407409, tzinfo=utc), max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='createpost',
            name='status',
            field=models.CharField(default='Publishing', max_length=10),
        ),
        migrations.AlterField(
            model_name='createpost',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]