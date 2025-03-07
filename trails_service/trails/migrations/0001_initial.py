# Generated by Django 5.1.6 on 2025-03-05 19:16

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=255)),
                ('difficulty', models.CharField(choices=[('easy', 'Fácil'), ('medium', 'Médio'), ('hard', 'Difícil')], max_length=50)),
                ('length_km', models.FloatField()),
                ('category_id', models.IntegerField()),
                ('date_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('image', models.ImageField(blank=True, help_text='Imagem representativa da trilha', null=True, upload_to='trail_images/')),
            ],
        ),
    ]
