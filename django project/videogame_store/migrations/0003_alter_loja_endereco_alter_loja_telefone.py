# Generated by Django 4.1.7 on 2023-03-30 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videogame_store', '0002_loja'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loja',
            name='endereco',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='loja',
            name='telefone',
            field=models.CharField(max_length=100),
        ),
    ]
