# Generated by Django 2.2.10 on 2020-05-13 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0012_auto_20200508_1943'),
    ]

    operations = [
        migrations.AddField(
            model_name='charttable',
            name='req_not_stared_units',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
