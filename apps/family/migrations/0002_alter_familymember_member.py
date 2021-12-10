# Generated by Django 3.2.9 on 2021-12-09 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('family', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familymember',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='family_members', to='family.member', verbose_name='member'),
        ),
    ]