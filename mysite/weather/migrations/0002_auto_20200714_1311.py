# Generated by Django 3.0.8 on 2020-07-14 10:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'ordering': ['-id'], 'verbose_name': 'City', 'verbose_name_plural': 'Cities'},
        ),
    ]
