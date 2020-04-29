# Generated by Django 2.2.10 on 2020-04-29 16:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0009_auto_20200420_2209'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='table',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='department',
            name='table_count',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='UserPassed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_passed', models.BooleanField(default=False)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='src.Course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
