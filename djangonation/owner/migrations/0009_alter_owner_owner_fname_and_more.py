# Generated by Django 4.0.1 on 2022-01-29 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0008_alter_owner_owner_inventory_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='owner_fname',
            field=models.CharField(default='bhushan', max_length=30),
        ),
        migrations.AlterField(
            model_name='owner',
            name='owner_inventory_city',
            field=models.CharField(default='bangalore', max_length=30),
        ),
        migrations.AlterField(
            model_name='owner',
            name='owner_inventory_name',
            field=models.CharField(default='inventory', max_length=30),
        ),
        migrations.AlterField(
            model_name='owner',
            name='owner_lname',
            field=models.CharField(default='poal', max_length=30),
        ),
        migrations.AlterField(
            model_name='owner',
            name='owner_password',
            field=models.CharField(default='male', max_length=30),
        ),
        migrations.AlterField(
            model_name='owner',
            name='owner_sex',
            field=models.CharField(default='male', max_length=10),
        ),
    ]