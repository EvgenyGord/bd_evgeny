# Generated by Django 4.2.5 on 2023-09-21 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0018_alter_movie_director'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(related_name='movies', to='movie_app.actor'),
        ),
    ]