# Generated by Django 2.2.6 on 2019-10-29 02:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='CapitalCity',
            fields=[
                ('cname', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('state', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='WebApp.State')),
            ],
        ),
    ]
