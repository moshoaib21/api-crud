# Generated by Django 4.1 on 2022-09-03 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0004_rename_price_hotel_star'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='star',
            field=models.IntegerField(),
        ),
    ]
