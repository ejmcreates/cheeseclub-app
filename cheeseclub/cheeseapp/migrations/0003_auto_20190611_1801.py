# Generated by Django 2.2 on 2019-06-11 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cheeseapp', '0002_auto_20190611_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cheese',
            name='cheeseentrydate',
            field=models.DateField(blank=True),
        ),
    ]
