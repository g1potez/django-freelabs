# Generated by Django 3.2.12 on 2022-03-17 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mynewuser', '0008_alter_users_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Users',
        ),
    ]
