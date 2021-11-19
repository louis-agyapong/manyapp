# Generated by Django 3.2.9 on 2021-11-19 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='members',
            field=models.ManyToManyField(related_name='groups', through='member.Membership', to='member.Member'),
        ),
    ]
