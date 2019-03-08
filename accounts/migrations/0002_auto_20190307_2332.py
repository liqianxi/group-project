# Generated by Django 2.1.7 on 2019-03-07 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FriendList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='userprofile',
            name='username',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='city',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='host',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddIndex(
            model_name='userprofile',
            index=models.Index(fields=['user'], name='usr_idx'),
        ),
    ]
