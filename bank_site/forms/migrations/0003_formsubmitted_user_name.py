# Generated by Django 4.1.4 on 2022-12-07 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0002_formsubmitted'),
    ]

    operations = [
        migrations.AddField(
            model_name='formsubmitted',
            name='user_name',
            field=models.CharField(default='hello', max_length=250),
            preserve_default=False,
        ),
    ]