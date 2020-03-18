# Generated by Django 2.2.5 on 2020-03-11 15:32

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=20)),
                ('isDropdown', models.BooleanField(default=False)),
                ('url', models.CharField(blank=True, max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='SubMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=20)),
                ('url', models.CharField(blank=True, max_length=40)),
                ('menuId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='IntranetUser.Menu')),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=40)),
                ('url', models.CharField(blank=True, max_length=40)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('categoryId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='IntranetUser.Category')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='menuId',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='IntranetUser.Menu'),
        ),
        migrations.AddField(
            model_name='category',
            name='subMenuId',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='IntranetUser.SubMenu'),
        ),
    ]
