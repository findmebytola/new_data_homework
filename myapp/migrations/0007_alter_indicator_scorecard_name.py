# Generated by Django 3.2.8 on 2021-10-19 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20211019_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indicator',
            name='scorecard_name',
            field=models.CharField(max_length=255),
        ),
    ]
