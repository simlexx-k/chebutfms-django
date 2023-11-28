# Generated by Django 4.2.7 on 2023-11-28 08:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fms', '0003_salarydeduction'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeaSubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_in_kgs', models.DecimalField(decimal_places=2, max_digits=10)),
                ('submission_date', models.DateField()),
                ('farmer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fms.farmer')),
            ],
        ),
    ]