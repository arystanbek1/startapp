# Generated by Django 4.2.4 on 2023-08-30 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_raiting_alter_organization_finished_project_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='status_account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.status_account', verbose_name='Статус подписки'),
        ),
    ]