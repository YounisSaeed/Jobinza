# Generated by Django 2.2.10 on 2020-02-29 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_relatedindustry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createpost',
            name='related_industry',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.relatedIndustry'),
        ),
    ]
