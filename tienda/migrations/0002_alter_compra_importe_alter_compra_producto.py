# Generated by Django 4.1.3 on 2022-11-21 07:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='importe',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='compra',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tienda.producto'),
        ),
    ]
