# Generated by Django 3.1.4 on 2020-12-30 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0004_auto_20201230_1106'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='bookmarks',
            field=models.ManyToManyField(to='portal.Paper'),
        ),
    ]
