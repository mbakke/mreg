# Generated by Django 3.2.4 on 2021-06-09 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authtoken', '0003_tokenproxy'),
        ('mreg', '0011_alter_bacnetid_host'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExpiringToken',
            fields=[
                ('token_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='authtoken.token')),
                ('last_used', models.DateTimeField(auto_now=True)),
            ],
            bases=('authtoken.token',),
        ),
    ]
