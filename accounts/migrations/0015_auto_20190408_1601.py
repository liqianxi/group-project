# Generated by Django 2.1.7 on 2019-04-08 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_merge_20190408_0738'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='visibleTo',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user_id',
            field=models.URLField(default=''),
        ),
    ]