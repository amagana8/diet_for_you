# Generated by Django 3.0 on 2020-07-26 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20200725_2339'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='foodtable',
            name='id',
        ),
        migrations.AddField(
            model_name='foodtable',
            name='foodId',
            field=models.IntegerField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
