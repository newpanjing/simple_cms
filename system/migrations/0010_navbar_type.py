# Generated by Django 2.2 on 2019-07-06 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0009_auto_20190702_2103'),
    ]

    operations = [
        migrations.AddField(
            model_name='navbar',
            name='type',
            field=models.IntegerField(choices=[(0, '电脑'), (1, '手机')], default=0, verbose_name='类型'),
        ),
    ]
