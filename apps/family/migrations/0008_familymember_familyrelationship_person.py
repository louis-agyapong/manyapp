# Generated by Django 3.2.9 on 2021-12-10 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('family', '0007_auto_20211210_1215'),
    ]

    operations = [
        migrations.CreateModel(
            name='FamilyRelationship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
            ],
            options={
                'verbose_name': 'family relationship',
                'verbose_name_plural': 'family relationships',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
            ],
            options={
                'verbose_name': 'member',
                'verbose_name_plural': 'members',
            },
        ),
        migrations.CreateModel(
            name='FamilyMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='family_members', to='family.person', verbose_name='member')),
                ('relation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='family_relations', to='family.familyrelationship', verbose_name='relation')),
                ('relative', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='family_relatives', to='family.person', verbose_name='relative')),
            ],
        ),
    ]
