# Generated by Django 4.1.1 on 2022-10-02 19:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_remove_book_location_book_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='location',
        ),
        migrations.AddField(
            model_name='book',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='booking.location'),
        ),
    ]