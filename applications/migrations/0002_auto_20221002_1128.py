# Generated by Django 2.2.26 on 2022-10-02 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app',
            name='framework',
            field=models.CharField(choices=[('Django', 'Django'), ('React Native', 'React Native')], max_length=256),
        ),
        migrations.AlterField(
            model_name='app',
            name='type',
            field=models.CharField(choices=[('Web', 'Web'), ('Mobile', 'Mobile')], max_length=256),
        ),
    ]
