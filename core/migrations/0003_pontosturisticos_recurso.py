# Generated by Django 4.1.4 on 2022-12-20 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atracoes', '0003_alter_recursos_descricao_alter_recursos_horario_func_and_more'),
        ('core', '0002_alter_pontosturisticos_provado'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontosturisticos',
            name='recurso',
            field=models.ManyToManyField(to='atracoes.recursos'),
        ),
    ]
