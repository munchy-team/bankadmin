# Generated by Django 4.0.5 on 2022-06-19 11:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_alter_transaction_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='time',
        ),
        migrations.AddField(
            model_name='transaction',
            name='status_time',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
