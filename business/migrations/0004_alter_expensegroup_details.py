# Generated by Django 4.0.2 on 2022-06-19 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0003_alter_expensegroup_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expensegroup',
            name='details',
            field=models.CharField(max_length=30),
        ),
    ]