# Generated by Django 4.2.4 on 2024-03-29 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_alter_members_week_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='Useremail',
            field=models.EmailField(max_length=200),
        ),
        migrations.AlterField(
            model_name='members',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='members',
            name='password',
            field=models.CharField(max_length=100),
        ),
    ]
