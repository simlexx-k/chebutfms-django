# Generated by Django 4.2.7 on 2023-11-29 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fms', '0017_teasubmission_submission_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teasubmission',
            old_name='field_manager',
            new_name='user',
        ),
    ]