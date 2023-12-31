# Generated by Django 4.2.2 on 2023-06-30 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shipments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shipper_name', models.CharField(max_length=40)),
                ('taxes_payments', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cargo_description', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('date_depature', models.DateTimeField(auto_now_add=True)),
                ('arrival_date', models.DateTimeField(auto_now=True)),
                ('weight', models.PositiveIntegerField()),
            ],
        ),
    ]
