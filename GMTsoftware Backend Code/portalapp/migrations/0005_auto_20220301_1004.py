# Generated by Django 3.2.8 on 2022-03-01 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portalapp', '0004_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(blank=True, default='', max_length=250)),
                ('lastName', models.CharField(blank=True, default='', max_length=250)),
                ('email', models.CharField(max_length=250, unique=True)),
                ('phoneNos', models.CharField(blank=True, default='', max_length=250)),
                ('registerCourse', models.CharField(blank=True, default='', max_length=250)),
                ('address', models.CharField(blank=True, default='', max_length=250)),
            ],
        ),
        migrations.DeleteModel(
            name='Userprofile',
        ),
    ]
