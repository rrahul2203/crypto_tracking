# Generated by Django 2.2 on 2022-09-20 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('price', models.CharField(blank=True, max_length=200, null=True)),
                ('market_cap', models.CharField(blank=True, max_length=200, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
