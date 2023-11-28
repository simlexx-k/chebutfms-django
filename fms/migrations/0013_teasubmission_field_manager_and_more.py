# Generated by Django 4.2.7 on 2023-11-28 09:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fms', '0012_alter_payment_max_salary_advance_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='teasubmission',
            name='field_manager',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='teasubmission',
            name='submission_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]