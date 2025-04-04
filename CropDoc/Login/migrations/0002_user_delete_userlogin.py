# Generated by Django 5.1.6 on 2025-04-04 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('Uid', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=150, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('Location', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='UserLogin',
        ),
    ]
