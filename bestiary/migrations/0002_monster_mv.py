# Generated by Django 3.2.9 on 2021-11-29 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bestiary', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='monster',
            name='MV',
            field=models.CharField(default='0', max_length=25),
            preserve_default=False,
        ),
    ]
