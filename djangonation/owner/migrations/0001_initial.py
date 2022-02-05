# Generated by Django 4.0.1 on 2022-01-27 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('owner_fname', models.CharField(max_length=30)),
                ('owner_lname', models.CharField(max_length=30)),
                ('owner_sex', models.CharField(max_length=10)),
                ('owner_email', models.EmailField(max_length=30, primary_key=True, serialize=False)),
                ('owner_password', models.CharField(max_length=30)),
                ('owner_inventory_name', models.CharField(max_length=30)),
                ('owner_inventory_city', models.CharField(max_length=30)),
            ],
        ),
    ]
