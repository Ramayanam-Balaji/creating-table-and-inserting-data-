# Generated by Django 4.2.1 on 2023-06-16 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='capital',
            name='id',
        ),
        migrations.AlterField(
            model_name='capital',
            name='capital_name',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
