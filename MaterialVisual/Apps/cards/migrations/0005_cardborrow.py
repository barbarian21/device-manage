# Generated by Django 3.2.6 on 2022-04-04 14:49

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('cards', '0004_auto_20211228_1140'),
    ]

    operations = [
        migrations.CreateModel(
            name='CardBorrow',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='板卡编号')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='添加时间')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('remark', models.TextField(blank=True, null=True, verbose_name='备注信息')),
                ('reason', models.TextField(verbose_name='借用理由')),
                ('time_borrowed', models.DateTimeField(null=True, verbose_name='借用时间')),
                ('time_end', models.DateTimeField(blank=True, null=True, verbose_name='归还时间')),
                ('is_return', models.BooleanField(default=False, verbose_name='是否归还')),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cardborrow', to='cards.cardmodel', verbose_name='板卡借用')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.deviceuser', verbose_name='使用者')),
            ],
            options={
                'verbose_name': '板卡借用',
                'verbose_name_plural': '板卡借用',
            },
        ),
    ]
