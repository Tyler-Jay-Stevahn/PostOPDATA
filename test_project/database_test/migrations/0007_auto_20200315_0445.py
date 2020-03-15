# Generated by Django 3.0.4 on 2020-03-15 09:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('database_test', '0006_auto_20200315_0348'),
    ]

    operations = [
        migrations.CreateModel(
            name='registrationdata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='database',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2020, 3, 15, 9, 45, 36, 978314, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='employees',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2020, 3, 15, 9, 45, 37, 28716, tzinfo=utc)),
        ),
    ]
