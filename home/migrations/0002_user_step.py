# Generated by Django 4.0.3 on 2022-03-09 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='step',
            field=models.IntegerField(default=0),
        ),
    ]
