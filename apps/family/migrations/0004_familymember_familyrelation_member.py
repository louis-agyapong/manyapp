# Generated by Django 3.2.9 on 2021-12-09 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('family', '0003_auto_20211209_1448'),
    ]

    operations = [
        migrations.CreateModel(
            name='FamilyRelation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
            ],
            options={
                'verbose_name': 'family relation',
                'verbose_name_plural': 'family relations',
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('age', models.IntegerField(verbose_name='age')),
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
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='family_members', to='family.member', verbose_name='member')),
                ('relation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='family.familyrelation', verbose_name='relation')),
                ('relatives', models.ManyToManyField(related_name='relatives', to='family.Member', verbose_name='family members')),
            ],
            options={
                'verbose_name': 'family member',
                'verbose_name_plural': 'family members',
            },
        ),
    ]
