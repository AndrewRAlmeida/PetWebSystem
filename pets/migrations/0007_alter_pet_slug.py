# Generated by Django 4.1.6 on 2023-05-16 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0006_alter_pet_options_pet_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='slug',
            field=models.SlugField(max_length=60, unique=True),
        ),
    ]