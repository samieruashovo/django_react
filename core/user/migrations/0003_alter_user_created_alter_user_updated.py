# Generated by Django 4.0.1 on 2023-06-16 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_user', '0002_alter_user_groups_alter_user_user_permissions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
