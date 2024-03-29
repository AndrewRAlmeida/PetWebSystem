# Generated by Django 4.1.6 on 2023-03-31 02:56

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ativo', models.BooleanField(default=True)),
                ('nome', models.CharField(max_length=60, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='pet',
            name='ativo',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='pet',
            name='castrado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='pet',
            name='cor',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='pet',
            name='descricao',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pet',
            name='dono',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pet',
            name='idade',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pet',
            name='raca',
            field=models.CharField(blank=True, help_text='use SRD caso não saiba ou não exista uma raça específica', max_length=60, null=True, verbose_name='Raça'),
        ),
        migrations.AddField(
            model_name='pet',
            name='vacinado',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='Imagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', sorl.thumbnail.fields.ImageField(blank=True, upload_to='pets')),
                ('perfil', models.BooleanField(verbose_name='Foto principal')),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pets.pet')),
            ],
            options={
                'verbose_name': 'Imagem',
                'verbose_name_plural': 'Imagens',
            },
        ),
        migrations.AddField(
            model_name='pet',
            name='categoria',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pets.categoria'),
            preserve_default=False,
        ),
    ]
