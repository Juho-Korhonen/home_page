# Generated by Django 4.0.3 on 2022-06-21 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('explanation', models.TextField(max_length=200)),
                ('github_link', models.CharField(max_length=100)),
            ],
        ),
    ]