# Generated by Django 2.2.26 on 2022-10-04 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0003_auto_20221003_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app',
            name='domain_name',
            field=models.CharField(blank=True, max_length=253, null=True),
        ),
    ]