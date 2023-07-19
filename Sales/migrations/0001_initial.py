# Generated by Django 4.2.3 on 2023-07-12 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('price', models.DecimalField(decimal_places=0, max_digits=9)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('stock', models.PositiveIntegerField()),
            ],
        ),
    ]
