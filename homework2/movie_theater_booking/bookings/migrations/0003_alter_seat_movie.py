# Generated by Django 4.2.11 on 2025-03-03 06:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0002_seat_movie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seat',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seats', to='bookings.movie'),
        ),
    ]
