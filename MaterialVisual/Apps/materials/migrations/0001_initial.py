# Generated by Django 3.2.6 on 2021-11-07 14:04

import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MaterialsModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='编号')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='添加时间')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('quarter', models.CharField(max_length=50, verbose_name='采购季度')),
                ('price', models.FloatField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='单价')),
                ('link', models.CharField(blank=True, max_length=100, null=True, verbose_name='链接')),
                ('name', models.CharField(max_length=50, verbose_name='物品名称')),
                ('detail', models.TextField(blank=True, null=True, verbose_name='详细描述')),
                ('remark', models.TextField(blank=True, null=True, verbose_name='备注信息')),
                ('residue', models.IntegerField(blank=True, null=True, verbose_name='剩余数量')),
            ],
            options={
                'verbose_name': '耗材使用',
                'verbose_name_plural': '耗材使用',
            },
        ),
        migrations.CreateModel(
            name='PurchaseModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='编号')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='添加时间')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('quarter', models.CharField(max_length=50, verbose_name='采购季度')),
                ('price', models.FloatField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='单价')),
                ('link', models.CharField(blank=True, max_length=100, null=True, verbose_name='链接')),
                ('name', models.CharField(max_length=50, verbose_name='物品名称')),
                ('detail', models.TextField(blank=True, null=True, verbose_name='详细描述')),
                ('remark', models.TextField(blank=True, null=True, verbose_name='备注信息')),
                ('reason', models.CharField(max_length=100, verbose_name='申请理由')),
            ],
            options={
                'verbose_name': '采购申请',
                'verbose_name_plural': '采购申请',
            },
        ),
    ]
