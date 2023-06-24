# Generated by Django 4.2.2 on 2023-06-22 10:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('i_d', models.CharField(max_length=50, unique=True)),
                ('is_waiting', models.BooleanField(default=True)),
                ('moves', models.CharField(max_length=1000)),
                ('player1', models.ForeignKey(default='default_player_1', on_delete=django.db.models.deletion.CASCADE, related_name='player1', to=settings.AUTH_USER_MODEL)),
                ('player2', models.ForeignKey(default='default_player_2', on_delete=django.db.models.deletion.CASCADE, related_name='player2', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
