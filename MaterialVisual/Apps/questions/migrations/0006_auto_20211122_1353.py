# Generated by Django 3.2.6 on 2021-11-22 13:53

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0005_alter_attachment_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='编号')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('remark', models.TextField(blank=True, null=True, verbose_name='备注信息')),
                ('type', models.CharField(blank=True, choices=[('0', 'UAT'), ('1', 'UXT'), ('2', 'BUG'), ('3', 'OTHER')], default='0', max_length=5, null=True, verbose_name='类别')),
                ('title', models.CharField(max_length=100, null=True, verbose_name='标题')),
                ('detail', models.TextField(null=True, verbose_name='详细描述')),
                ('user', models.CharField(max_length=20, null=True, verbose_name='创建者')),
                ('version', models.CharField(max_length=50, null=True, verbose_name='版本')),
            ],
            options={
                'verbose_name': 'UAXT信息',
                'verbose_name_plural': 'UAXT信息',
            },
        ),
        migrations.DeleteModel(
            name='BugCommentModel',
        ),
        migrations.DeleteModel(
            name='OtherQuestionsModel',
        ),
        migrations.RemoveField(
            model_name='attachment',
            name='image',
        ),
        migrations.RemoveField(
            model_name='attachment',
            name='uaxt',
        ),
        migrations.AddField(
            model_name='attachment',
            name='attach',
            field=models.FileField(null=True, upload_to='static/images/questions/%Y-%d-%s/', verbose_name='附件'),
        ),
        migrations.DeleteModel(
            name='UaxTModel',
        ),
        migrations.AddField(
            model_name='attachment',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='attachments', to='questions.questionmodel'),
        ),
    ]
