# Generated by Django 2.2.4 on 2019-10-13 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('price', models.IntegerField()),
                ('wallpaper', models.ImageField(upload_to='wall/')),
            ],
        ),
    ]
