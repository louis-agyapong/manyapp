# Generated by Django 4.0 on 2021-12-12 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_enrollment_unique_enrollment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
