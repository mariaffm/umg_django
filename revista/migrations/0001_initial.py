# Generated by Django 4.1 on 2022-09-16 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publicaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100, verbose_name='Nombre')),
                ('apellido', models.CharField(blank=True, max_length=100, verbose_name='Apellido')),
                ('tipoNoticia', models.CharField(blank=True, max_length=100, verbose_name='Tipo_Noticia')),
                ('creacion', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
