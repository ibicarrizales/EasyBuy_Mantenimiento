# Generated by Django 5.0.6 on 2024-07-16 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('COMPRA_VENTA', '0003_favorito'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='favorito',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='Favorito',
        ),
    ]
