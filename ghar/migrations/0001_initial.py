# Generated by Django 3.0.5 on 2020-05-05 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(default='', max_length=50)),
                ('message', models.CharField(default='', max_length=500)),
            ],
        ),
    ]