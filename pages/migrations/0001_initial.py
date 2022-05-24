# Generated by Django 4.0.4 on 2022-04-12 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_id', models.IntegerField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('original_value', models.FloatField()),
                ('collaborator_owner', models.CharField(max_length=30)),
                ('social_bussiness_name', models.CharField(max_length=40)),
                ('CNPJ', models.IntegerField()),
            ],
        ),
    ]
