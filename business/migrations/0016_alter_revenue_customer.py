# Generated by Django 4.0.2 on 2022-06-16 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0015_remove_revenue_customer_revenue_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='revenue',
            name='customer',
            field=models.ManyToManyField(to='business.Customers'),
        ),
    ]