# Generated by Django 3.0.8 on 2020-07-30 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0010_auto_20200731_0041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
