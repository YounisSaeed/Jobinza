# Generated by Django 2.2.10 on 2020-03-07 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicant', '0003_auto_20200307_0236'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phonenumber', models.CharField(blank=True, max_length=50)),
                ('address', models.CharField(blank=True, max_length=50)),
            ],
        ),
    ]
