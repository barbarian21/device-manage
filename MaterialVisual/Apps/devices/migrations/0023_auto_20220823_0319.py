# Generated by Django 3.2.6 on 2022-08-23 03:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_worknotes'),
        ('devices', '0022_auto_20220811_0308'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='current_user',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.DO_NOTHING, to='users.deviceuser', verbose_name='当前使用者'),
        ),
        migrations.AddField(
            model_name='historicaldevice',
            name='current_user',
            field=models.ForeignKey(blank=True, db_constraint=False, default=2, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='users.deviceuser', verbose_name='当前使用者'),
        ),
    ]
