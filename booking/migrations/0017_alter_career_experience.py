# Generated by Django 3.2.15 on 2022-10-06 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0016_career_experience'),
    ]

    operations = [
        migrations.AlterField(
            model_name='career',
            name='experience',
            field=models.IntegerField(),
        ),
    ]