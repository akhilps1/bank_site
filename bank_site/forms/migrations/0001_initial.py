# Generated by Django 4.1.4 on 2022-12-07 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccountForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=250)),
                ('user_age', models.CharField(max_length=250)),
                ('user_dob', models.CharField(max_length=250)),
                ('user_gender', models.CharField(max_length=250)),
                ('user_email', models.EmailField(max_length=254)),
                ('user_phone_no', models.CharField(max_length=250)),
                ('user_address', models.TextField()),
                ('district', models.CharField(max_length=250)),
                ('branch', models.CharField(max_length=250)),
                ('debit_card', models.BooleanField(default=False)),
                ('credit_card', models.BooleanField(default=False)),
                ('cheque_book', models.BooleanField(default=False)),
            ],
        ),
    ]
