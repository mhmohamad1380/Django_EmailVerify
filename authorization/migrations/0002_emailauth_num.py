# Generated by Django 3.2.5 on 2021-07-21 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailauth',
            name='num',
            field=models.IntegerField(null=True),
        ),
    ]