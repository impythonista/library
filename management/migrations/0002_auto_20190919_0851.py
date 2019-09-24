# Generated by Django 2.2.5 on 2019-09-19 08:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='readerstracker',
            old_name='created_dt',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='readerstracker',
            old_name='udpated_dt',
            new_name='updated',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='created_dt',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='udpated_dt',
            new_name='updated',
        ),
        migrations.AddField(
            model_name='bookcatalog',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2019, 9, 19, 8, 51, 45, 932870, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bookcatalog',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]