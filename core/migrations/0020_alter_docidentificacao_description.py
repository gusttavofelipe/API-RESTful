# Generated by Django 4.1.4 on 2023-01-31 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_alter_docidentificacao_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docidentificacao',
            name='description',
            field=models.CharField(max_length=99),
        ),
    ]
