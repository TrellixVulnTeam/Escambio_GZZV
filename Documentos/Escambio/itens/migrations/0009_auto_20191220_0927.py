# Generated by Django 3.0.1 on 2019-12-20 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itens', '0008_auto_20191220_0917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incluir_item',
            name='imagem1',
            field=models.ImageField(blank=True, upload_to='static'),
        ),
    ]
