# Generated by Django 4.1.3 on 2022-12-04 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_rename_posts_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='likes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('post_liked', models.CharField(max_length=500)),
            ],
        ),
    ]
