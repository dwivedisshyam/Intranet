# Generated by Django 2.2.5 on 2020-03-11 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IntranetUser', '0002_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='deptName',
            field=models.CharField(max_length=60),
        ),
    ]
