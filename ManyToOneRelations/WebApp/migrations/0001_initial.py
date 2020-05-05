# Generated by Django 2.2.6 on 2019-10-30 02:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tname', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('pname', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebApp.Team')),
            ],
        ),
    ]
