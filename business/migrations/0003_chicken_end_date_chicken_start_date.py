# Generated by Django 4.0.2 on 2022-06-16 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0002_alter_chicken_date_alter_deaths_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='chicken',
            name='end_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='chicken',
            name='start_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
