# Generated by Django 4.2.2 on 2023-06-26 00:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ordenamiento', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barrio',
            name='parroquia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parroquiass', to='ordenamiento.parroquia'),
        ),
    ]
