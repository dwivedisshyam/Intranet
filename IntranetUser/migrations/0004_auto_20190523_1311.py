# Generated by Django 2.2.1 on 2019-05-23 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('IntranetUser', '0003_auto_20190523_1148'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subcategory',
            old_name='hyperlink',
            new_name='content',
        ),
    ]
