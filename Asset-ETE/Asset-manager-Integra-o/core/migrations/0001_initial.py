# Generated by Django 4.2.4 on 2023-08-22 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DadoSensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nivel_agua', models.FloatField()),
                ('data_leitura', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
