# Generated by Django 3.0.4 on 2020-03-15 08:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('database_test', '0005_auto_20200315_0219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='database',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2020, 3, 15, 8, 48, 27, 852748, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='employees',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2020, 3, 15, 8, 48, 27, 908750, tzinfo=utc)),
        ),
    ]
