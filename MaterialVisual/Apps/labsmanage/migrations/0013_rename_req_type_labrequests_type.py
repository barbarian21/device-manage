# Generated by Django 3.2.6 on 2023-01-13 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labsmanage', '0012_rename_type_labrequests_req_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='labrequests',
            old_name='req_type',
            new_name='type',
        ),
    ]
