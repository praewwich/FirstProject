# Generated by Django 2.1.4 on 2019-01-08 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Count',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='Price',
            field=models.IntegerField(),
        ),
    ]