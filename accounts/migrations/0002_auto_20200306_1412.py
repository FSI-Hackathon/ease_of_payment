# Generated by Django 2.1.2 on 2020-03-06 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='account_balance',
            field=models.DecimalField(decimal_places=2, default=1000.0, max_digits=15),
        ),
    ]
