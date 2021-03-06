# Generated by Django 3.0 on 2020-02-23 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tinderforeduapp', '0011_auto_20200223_1512'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='star',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='username',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='comment',
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_value',
            field=models.CharField(max_length=200, null=True, verbose_name='comment'),
        ),
        migrations.AddField(
            model_name='comment',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='tinderforeduapp.Userinfo', verbose_name='profile'),
        ),
    ]
