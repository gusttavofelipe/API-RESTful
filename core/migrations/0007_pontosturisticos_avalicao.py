# Generated by Django 4.1.4 on 2022-12-20 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avaliacoes', '0001_initial'),
        ('core', '0006_pontosturisticos_comentario'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontosturisticos',
            name='avalicao',
            field=models.ManyToManyField(to='avaliacoes.avalicao'),
        ),
    ]
