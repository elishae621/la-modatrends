# Generated by Django 3.1 on 2021-01-17 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='label',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]