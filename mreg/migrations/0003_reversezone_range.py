# Generated by Django 2.1.7 on 2019-02-19 10:40

from django.db import migrations, models
import mreg.validators


class Migration(migrations.Migration):

    dependencies = [
        ('mreg', '0002_forwardzonedelegation_reversezonedelegation'),
    ]

    operations = [
        migrations.AddField(
            model_name='reversezone',
            name='range',
            field=models.TextField(blank=True, unique=True, validators=[mreg.validators.validate_network]),
        ),
    ]
