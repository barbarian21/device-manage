# Generated by Django 3.2.6 on 2021-12-01 13:25

import django.core.serializers.json
import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0007_alter_budgetmodel_budget_body'),
    ]

    operations = [
        migrations.CreateModel(
            name='OtherMaterials',
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
                ('users', models.JSONField(blank=True, default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder, null=True, verbose_name='使用者')),
                ('residue', models.IntegerField(blank=True, null=True, verbose_name='剩余数量')),
            ],
            options={
                'verbose_name': '其他耗材',
                'verbose_name_plural': '其他耗材',
            },
        ),
    ]
