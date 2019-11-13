# Generated by Django 2.2.5 on 2019-11-01 03:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='state',
            fields=[
                ('sname', models.CharField(max_length=255, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='capitalcity',
            fields=[
                ('CNAME', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('state', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='webapp.state')),
            ],
        ),
    ]
