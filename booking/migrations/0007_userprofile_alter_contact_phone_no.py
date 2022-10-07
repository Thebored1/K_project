# Generated by Django 4.1.1 on 2022-10-03 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0006_alter_book_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=2000, null=True)),
                ('phone_no', models.IntegerField(null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone_no',
            field=models.IntegerField(null=True),
        ),
    ]