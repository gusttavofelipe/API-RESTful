# Generated by Django 4.1.4 on 2022-12-28 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_alter_pontoturistico_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pontoturistico',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='imagens_pontos', verbose_name='Imagem'),
        ),
    ]
