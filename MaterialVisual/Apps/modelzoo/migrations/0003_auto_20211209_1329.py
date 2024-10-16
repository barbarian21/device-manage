# Generated by Django 3.2.6 on 2021-12-09 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modelzoo', '0002_auto_20211122_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachment',
            name='attach',
            field=models.FileField(blank=True, null=True, upload_to='static/uploads/modelzoo/%Y-%d-%d/', verbose_name='附件'),
        ),
        migrations.AlterField(
            model_name='attachment',
            name='report',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='attachments', to='modelzoo.reportmodel'),
        ),
        migrations.AlterField(
            model_name='releasemodel',
            name='note',
            field=models.TextField(blank=True, null=True, verbose_name='发布信息'),
        ),
        migrations.AlterField(
            model_name='releasemodel',
            name='url',
            field=models.URLField(blank=True, null=True, verbose_name='链接'),
        ),
        migrations.AlterField(
            model_name='releasemodel',
            name='version',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True, verbose_name='版本'),
        ),
        migrations.AlterField(
            model_name='reportmodel',
            name='detail',
            field=models.TextField(blank=True, null=True, verbose_name='详细描述'),
        ),
        migrations.AlterField(
            model_name='reportmodel',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='标题'),
        ),
        migrations.AlterField(
            model_name='reportmodel',
            name='user',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='创建者'),
        ),
        migrations.AlterField(
            model_name='reportmodel',
            name='version',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='版本'),
        ),
    ]
