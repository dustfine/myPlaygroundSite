# Generated by Django 2.1.4 on 2018-12-17 05:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_userinfo_emial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userinfo',
            old_name='emial',
            new_name='email',
        ),
    ]