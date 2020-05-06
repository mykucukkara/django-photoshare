# Generated by Django 3.0.4 on 2020-05-05 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='status',
            field=models.CharField(blank=True, choices=[('New', 'Yeni'), ('True', 'Evet'), ('False', 'Hayır')], max_length=10),
        ),
        migrations.AlterField(
            model_name='comment',
            name='subject',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
