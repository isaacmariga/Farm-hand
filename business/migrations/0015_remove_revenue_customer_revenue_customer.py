# Generated by Django 4.0.2 on 2022-06-16 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0014_customers_delete_editors_revenue_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='revenue',
            name='customer',
        ),
        migrations.AddField(
            model_name='revenue',
            name='customer',
            field=models.ManyToManyField(blank=True, null=True, to='business.Customers'),
        ),
    ]