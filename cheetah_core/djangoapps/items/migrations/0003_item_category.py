# Generated by Django 2.0.13 on 2019-04-21 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_auto_20190421_1524'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('A', 'Buyable'), ('B', 'Unavailable')], default='A', max_length=1, verbose_name='Item category'),
        ),
    ]
