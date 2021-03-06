# Generated by Django 3.1 on 2020-11-08 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('precio', models.IntegerField()),
                ('descripcion', models.TextField()),
                ('marca', models.CharField(max_length=20)),
                ('imagen', models.ImageField(null=True, upload_to='productos')),
            ],
        ),
    ]
