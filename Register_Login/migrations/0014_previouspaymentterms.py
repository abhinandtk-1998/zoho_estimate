# Generated by Django 4.2 on 2024-01-20 08:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Register_Login', '0013_notifications_time_alter_notifications_date_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='PreviousPaymentTerms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_term', models.CharField(blank=True, max_length=255, null=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='previous_plans', to='Register_Login.companydetails')),
                ('distributor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='previous_plans', to='Register_Login.distributordetails')),
            ],
        ),
    ]
