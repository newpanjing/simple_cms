# Generated by Django 2.2 on 2019-07-01 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0002_auto_20190701_1824'),
    ]

    operations = [
        migrations.AddField(
            model_name='navbar',
            name='sort',
            field=models.IntegerField(default=0, help_text='值越小排越前', verbose_name='排序'),
        ),
    ]
