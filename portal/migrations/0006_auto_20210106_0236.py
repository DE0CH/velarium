# Generated by Django 3.1.4 on 2021-01-06 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0005_user_bookmarks'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper',
            name='link',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='bookmarks',
            field=models.ManyToManyField(related_name='bookmarkers', to='portal.Paper'),
        ),
    ]
