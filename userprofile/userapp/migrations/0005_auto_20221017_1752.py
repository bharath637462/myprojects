# Generated by Django 3.2 on 2022-10-17 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0004_alter_userprofile_job'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user_id',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users', to='userapp.user'),
        ),
    ]
