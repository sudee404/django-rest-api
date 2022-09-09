# Generated by Django 4.1.1 on 2022-09-09 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('source_link', models.URLField()),
                ('web_link', models.URLField(null=True)),
                ('poster', models.ImageField(upload_to='')),
            ],
        ),
    ]