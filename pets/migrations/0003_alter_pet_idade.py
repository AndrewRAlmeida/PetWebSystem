# Generated by Django 4.1.6 on 2023-03-31 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0002_categoria_pet_ativo_pet_castrado_pet_cor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='idade',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]