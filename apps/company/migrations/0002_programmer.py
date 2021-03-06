# Generated by Django 3.2.9 on 2021-12-05 03:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Programmer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='programmers', to='company.company', verbose_name='company')),
            ],
        ),
    ]
