# Generated by Django 4.1 on 2024-01-16 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prdId', models.CharField(max_length=12, unique=True, verbose_name='Product ID')),
                ('used', models.IntegerField(default=0)),
            ],
        ),
    ]
