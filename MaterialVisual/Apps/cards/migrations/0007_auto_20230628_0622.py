# Generated by Django 3.2.6 on 2023-06-28 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0006_auto_20230112_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardmodel',
            name='version',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='存放位置'),
        ),
        migrations.AlterField(
            model_name='historicalcardmodel',
            name='version',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='存放位置'),
        ),
    ]
