# Generated by Django 3.1.1 on 2020-11-17 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mreg', '0008_auto_20201117_0947'),
        ('hostpolicy', '0002_hostpolicyrole_hosts'),
    ]

    operations = [
        migrations.AddField(
            model_name='hostpolicyrole',
            name='labels',
            field=models.ManyToManyField(blank=True, related_name='hostpolicyroles', to='mreg.Label'),
        ),
    ]
