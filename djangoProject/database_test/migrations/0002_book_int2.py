# Generated by Django 4.1.1 on 2022-09-16 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database_test', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='int2',
            field=models.IntegerField(null=True),
        ),
    ]
