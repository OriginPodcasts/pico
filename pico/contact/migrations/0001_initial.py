# Generated by Django 3.2.6 on 2022-02-13 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=255)),
                ('sent', models.DateTimeField(auto_now_add=True)),
                ('subject', models.CharField(max_length=100)),
                ('body', models.TextField()),
            ],
            options={
                'ordering': ('-sent',),
                'get_latest_by': 'sent',
            },
        ),
    ]
