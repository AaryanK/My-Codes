# Generated by Django 3.2.7 on 2021-11-09 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='ratings',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=0),
        ),
    ]