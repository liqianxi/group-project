# Generated by Django 2.1.7 on 2019-04-08 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20190403_0059'),
    ]

    operations = [
        migrations.AddField(
            model_name='postvisibleto',
            name='user_url',
            field=models.URLField(default=''),
        ),
        migrations.AlterUniqueTogether(
            name='postvisibleto',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='postvisibleto',
            name='user_id',
        ),
    ]
