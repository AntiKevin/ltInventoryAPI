# Generated by Django 4.1.3 on 2022-11-05 04:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LaborTools', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='maodeobra',
            name='vinculo',
        ),
    ]
