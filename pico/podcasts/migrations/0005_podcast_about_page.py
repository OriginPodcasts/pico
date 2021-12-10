# Generated by Django 3.2.6 on 2021-12-10 11:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('podcasts', '0004_auto_20210922_1631'),
    ]

    operations = [
        migrations.AddField(
            model_name='podcast',
            name='about_page',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='about_page_for', to='podcasts.page'),
        ),
    ]