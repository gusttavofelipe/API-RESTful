# Generated by Django 4.1.4 on 2022-12-21 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0003_alter_comentario_comentario_alter_comentario_usuario'),
        ('atracoes', '0004_rename_recursos_recurso'),
        ('enderecos', '0002_rename_enderereco_endereco'),
        ('avaliacoes', '0002_alter_avalicao_comentario_alter_avalicao_usuario'),
        ('core', '0009_rename_pontosturisticos_pontosturistico'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PontosTuristico',
            new_name='PontoTuristico',
        ),
    ]
