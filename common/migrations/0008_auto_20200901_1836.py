# Generated by Django 2.2.11 on 2020-09-01 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0007_tag_is_starter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='is_starter',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]