# Generated by Django 5.0.2 on 2024-02-19 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('sub_title', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
