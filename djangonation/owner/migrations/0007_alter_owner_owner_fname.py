# Generated by Django 4.0.1 on 2022-01-29 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0006_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='owner_fname',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
