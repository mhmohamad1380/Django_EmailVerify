# Generated by Django 3.2.5 on 2021-07-22 05:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0002_emailauth_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailauth',
            name='created_time',
            field=models.TimeField(auto_created=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
