# Generated by Django 4.1.6 on 2023-05-27 00:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0008_adocoes'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='adocoes',
            options={'ordering': ('-data_cadastro',), 'verbose_name': 'Adoçao', 'verbose_name_plural': 'Adoções'},
        ),
    ]
