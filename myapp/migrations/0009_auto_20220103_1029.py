# Generated by Django 3.0 on 2022-01-03 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_user_admin_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='block',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='delete',
            field=models.BooleanField(default=False),
        ),
    ]
