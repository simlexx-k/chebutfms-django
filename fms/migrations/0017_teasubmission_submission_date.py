# Generated by Django 4.2.7 on 2023-11-29 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fms', '0016_remove_teasubmission_submission_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='teasubmission',
            name='submission_date',
            field=models.DateField(auto_now=True),
        ),
    ]