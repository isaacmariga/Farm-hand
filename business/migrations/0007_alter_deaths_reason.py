# Generated by Django 4.0.2 on 2022-06-16 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0006_rename_projected_sp_chicken_projected_sp_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deaths',
            name='reason',
            field=models.TextField(max_length=300),
        ),
    ]