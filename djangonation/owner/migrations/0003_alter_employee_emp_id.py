# Generated by Django 4.0.1 on 2022-01-27 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0002_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='Emp_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
