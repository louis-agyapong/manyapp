# Generated by Django 3.2.9 on 2021-12-09 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('family', '0002_alter_familymember_member'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='relative',
            name='family_member',
        ),
        migrations.DeleteModel(
            name='FamilyMember',
        ),
        migrations.DeleteModel(
            name='Member',
        ),
        migrations.DeleteModel(
            name='Relative',
        ),
    ]
