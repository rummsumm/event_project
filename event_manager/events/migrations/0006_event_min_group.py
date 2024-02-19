# Generated by Django 5.0.2 on 2024-02-19 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_event_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='min_group',
            field=models.PositiveSmallIntegerField(choices=[(5, 'Small'), (10, 'Medium'), (15, 'Big'), (0, 'Unlimited')], default=0),
        ),
    ]