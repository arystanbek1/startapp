# Generated by Django 4.2.4 on 2023-08-09 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_organization_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organization',
            name='test',
        ),
    ]
