# Generated by Django 2.2.7 on 2019-12-09 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20191208_1258'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.TextField(max_length=300)),
                ('rank', models.IntegerField()),
                ('status', models.CharField(blank=True, choices=[('active', 'active'), ('', 'default')], max_length=100)),
                ('description', models.TextField()),
                ('text_one', models.CharField(max_length=200)),
                ('text_two', models.CharField(max_length=200)),
                ('text_three', models.CharField(max_length=200)),
                ('url', models.TextField()),
            ],
        ),
    ]