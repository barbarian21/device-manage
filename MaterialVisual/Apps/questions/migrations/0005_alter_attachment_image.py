# Generated by Django 3.2.6 on 2021-11-20 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0004_auto_20211119_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachment',
            name='image',
            field=models.ImageField(upload_to='static/images/questions/uaxt/', verbose_name='图片'),
        ),
    ]
