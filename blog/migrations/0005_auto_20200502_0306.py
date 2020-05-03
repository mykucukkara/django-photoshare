# Generated by Django 3.0.4 on 2020-05-02 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200501_0534'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='slug',
            field=models.SlugField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='blog',
            name='description',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='blog',
            name='keywords',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='category',
            name='keywords',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]