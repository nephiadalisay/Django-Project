# Generated by Django 3.0.8 on 2020-07-30 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0011_auto_20200731_0044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='image',
            field=models.ImageField(blank=True, default=False, null=True, upload_to=''),
        ),
    ]