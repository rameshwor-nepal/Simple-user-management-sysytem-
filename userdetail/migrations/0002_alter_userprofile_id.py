# Generated by Django 3.2.5 on 2021-07-22 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userdetail', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
