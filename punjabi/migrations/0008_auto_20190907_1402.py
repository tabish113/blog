# Generated by Django 2.2.4 on 2019-09-07 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('punjabi', '0007_order_room_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='payment',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='booking',
            name='status',
            field=models.CharField(default='', max_length=20),
        ),
    ]
