# Generated by Django 2.1.7 on 2019-03-08 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20190307_2332'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friendship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='PostVisibeTo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RenameModel(
            old_name='FriendList',
            new_name='Comment',
        ),
        migrations.RemoveIndex(
            model_name='userprofile',
            name='usr_idx',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='description',
            new_name='bio',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='username',
            new_name='displayName',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='website',
            new_name='github',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='user',
            new_name='user_id',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='city',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='phone',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='url',
            field=models.URLField(default=''),
        ),
        migrations.AddIndex(
            model_name='userprofile',
            index=models.Index(fields=['user_id'], name='usr_idx'),
        ),
    ]
