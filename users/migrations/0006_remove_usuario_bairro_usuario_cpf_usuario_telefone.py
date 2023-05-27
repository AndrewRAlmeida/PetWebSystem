# Generated by Django 4.1.6 on 2023-05-05 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_usuario_options_remove_usuario_date_joined_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='bairro',
        ),
        migrations.AddField(
            model_name='usuario',
            name='cpf',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='telefone',
            field=models.CharField(default=1, help_text='somente números', max_length=60),
            preserve_default=False,
        ),
    ]