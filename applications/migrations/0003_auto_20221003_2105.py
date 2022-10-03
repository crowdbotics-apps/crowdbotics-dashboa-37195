# Generated by Django 2.2.26 on 2022-10-03 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0002_auto_20221002_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='app',
            name='screenshot',
            field=models.URLField(blank=True, null=True),
        ),
    ]
