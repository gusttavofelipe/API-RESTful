# Generated by Django 4.1.4 on 2022-12-20 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_rename_provado_pontosturisticos_aprovado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pontosturisticos',
            name='descricao',
            field=models.TextField(verbose_name='Descrição'),
        ),
    ]
