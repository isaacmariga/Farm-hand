# Generated by Django 4.0.2 on 2022-06-29 17:03

import business.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0020_alter_batch_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenses',
            name='amount',
            field=models.IntegerField(default=business.models.Deaths.death_sum),
        ),
    ]