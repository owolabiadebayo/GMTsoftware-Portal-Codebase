# Generated by Django 3.2.8 on 2022-03-17 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portalapp', '0010_profile_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eachtask',
            name='course',
        ),
        migrations.AddField(
            model_name='eachtask',
            name='phone_nos',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='eachtask',
            name='Reviews',
            field=models.TextField(blank=True, default=''),
        ),
    ]
