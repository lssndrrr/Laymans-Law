# Generated by Django 5.0.3 on 2024-06-06 01:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('abogado', '0001_initial'),
        ('manggagawa', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='handles',
            name='case_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='manggagawa.cases'),
        ),
    ]
