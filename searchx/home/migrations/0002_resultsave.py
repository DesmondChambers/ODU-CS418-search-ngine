# Generated by Django 2.2 on 2020-11-19 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resultsave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField(blank=True, null=True)),
                ('title', models.TextField(blank=True, null=True)),
                ('relation_haspart', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
