# Generated by Django 2.2 on 2019-07-04 08:18

from django.db import migrations, models
import ueditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0009_auto_20190703_1614'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alias', models.CharField(db_index=True, max_length=256, verbose_name='别名')),
                ('title', models.CharField(max_length=256, verbose_name='标题')),
                ('keywords', models.CharField(blank=True, max_length=512, null=True, verbose_name='关键字')),
                ('description', models.CharField(blank=True, max_length=512, null=True, verbose_name='描述')),
                ('createDate', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('display', models.BooleanField(db_index=True, default=True, verbose_name='是否显示')),
                ('head', models.TextField(blank=True, null=True, verbose_name='头部脚本')),
                ('footer', models.TextField(blank=True, null=True, verbose_name='尾部脚本')),
            ],
            options={
                'verbose_name': '页面',
                'verbose_name_plural': '页面管理',
            },
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=ueditor.fields.RichTextField(verbose_name='内容'),
        ),
    ]
