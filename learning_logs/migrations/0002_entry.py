# Generated by Django 3.1.4 on 2020-12-29 16:12

import builtins
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('topic', models.ForeignKey(on_delete=builtins.callable, to='learning_logs.topic')),
            ],
            options={
                'verbose_name_plural': 'entrise',
            },
        ),
    ]
