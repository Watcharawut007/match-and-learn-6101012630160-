# Generated by Django 3.0.2 on 2020-02-12 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tinderforeduapp', '0009_auto_20200212_1744'),
    ]

    operations = [
        migrations.CreateModel(
            name='match_class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match', models.TextField(blank=True, max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='request_class',
            name='match_list',
        ),
        migrations.AddField(
            model_name='userinfo',
            name='match',
            field=models.ManyToManyField(to='tinderforeduapp.match_class'),
        ),
    ]
