# Generated by Django 3.0.2 on 2020-01-29 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tinderforeduapp', '0006_profile_college'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='age',
            field=models.TextField(blank=True, max_length=10),
        ),
    ]
