# Generated by Django 3.2.4 on 2021-06-13 20:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_alter_members_age'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Members',
            new_name='Member',
        ),
    ]
