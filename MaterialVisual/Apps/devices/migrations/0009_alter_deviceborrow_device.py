# Generated by Django 3.2.6 on 2021-11-18 05:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0008_alter_deviceborrow_device'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deviceborrow',
            name='device',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='devices', to='devices.device', verbose_name='借用的设备'),
        ),
    ]
