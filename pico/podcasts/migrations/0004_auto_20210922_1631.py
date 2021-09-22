# Generated by Django 3.2.6 on 2021-09-22 15:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('podcasts', '0003_podcast_short_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='podcast',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pages', to='podcasts.podcast'),
        ),
        migrations.AlterField(
            model_name='post',
            name='podcast',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to='podcasts.podcast'),
        ),
    ]