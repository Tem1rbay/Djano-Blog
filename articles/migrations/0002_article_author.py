# Generated by Django 4.1.5 on 2023-02-13 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.CharField(default='Admin', max_length=50),
        ),
    ]
