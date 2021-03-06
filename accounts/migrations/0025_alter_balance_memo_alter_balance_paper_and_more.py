# Generated by Django 4.0.5 on 2022-06-23 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0024_alter_transaction_approved_or_declined_by_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='balance',
            name='memo',
            field=models.CharField(blank=True, help_text='This is for the HTML form. Do not manually type anything here if you are a superuser or things will mess up.', max_length=100),
        ),
        migrations.AlterField(
            model_name='balance',
            name='paper',
            field=models.CharField(blank=True, help_text='This is for the HTML form. Do not manually type anything here if you are a superuser or things will mess up.', max_length=100),
        ),
        migrations.AlterField(
            model_name='balance',
            name='pencil',
            field=models.CharField(blank=True, help_text='This is for the HTML form. Do not manually type anything here if you are a superuser or things will mess up.', max_length=100),
        ),
        migrations.AlterField(
            model_name='balance',
            name='time',
            field=models.CharField(blank=True, help_text='This is for the HTML form. Do not manually type anything here if you are a superuser or things will mess up.', max_length=100),
        ),
        migrations.AlterField(
            model_name='balance',
            name='username',
            field=models.CharField(blank=True, help_text='This is for the HTML form. Do not manually type anything here if you are a superuser or things will mess up.', max_length=100),
        ),
    ]
