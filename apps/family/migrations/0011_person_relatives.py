# Generated by Django 3.2.9 on 2021-12-10 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('family', '0010_familymember_familyrelationship_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='relatives',
            field=models.ManyToManyField(related_name='_family_person_relatives_+', through='family.FamilyMember', to='family.Person', verbose_name='relatives'),
        ),
    ]