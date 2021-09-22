# Generated by Django 3.2.6 on 2021-09-22 11:14

from django.db import migrations, models
import django.db.models.deletion
import markdownx.models
import pico.podcasts.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=30, unique=True)),
            ],
            options={
                'verbose_name_plural': 'categories',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Directory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('icon', models.FileField(max_length=255, upload_to=pico.podcasts.models.Directory.upload_icon)),
                ('ordering', models.PositiveIntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'directories',
                'ordering': ('ordering',),
            },
        ),
        migrations.CreateModel(
            name='Podcast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=30, unique=True)),
                ('domain', models.CharField(max_length=100, unique=True)),
                ('rss_feed_url', models.URLField(max_length=255, unique=True, verbose_name='RSS feed URL')),
                ('artwork', models.ImageField(max_length=255, upload_to=pico.podcasts.models.Podcast.upload_artwork)),
                ('subtitle', models.CharField(blank=True, max_length=255, null=True)),
                ('description', markdownx.models.MarkdownxField()),
                ('twitter_username', models.CharField(blank=True, max_length=30, null=True)),
                ('facebook_username', models.CharField(blank=True, max_length=30, null=True)),
                ('instagram_username', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField(default=1)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('artwork', models.ImageField(blank=True, max_length=255, null=True, upload_to=pico.podcasts.models.Season.upload_artwork)),
                ('summary', models.TextField(blank=True, null=True)),
                ('description', markdownx.models.MarkdownxField(blank=True, null=True)),
                ('podcast', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seasons', to='podcasts.podcast')),
            ],
            options={
                'ordering': ('number',),
                'unique_together': {('number', 'podcast')},
            },
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(max_length=255, upload_to=pico.podcasts.models.Host.upload_photo)),
                ('number', models.PositiveIntegerField(default=1)),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=30, unique=True)),
                ('biography', markdownx.models.MarkdownxField(blank=True, null=True)),
                ('podcasts', models.ManyToManyField(related_name='hosts', to='podcasts.Podcast')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='SubscriptionLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(max_length=255, verbose_name='URL')),
                ('directory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entries', to='podcasts.directory')),
                ('podcast', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscription_links', to='podcasts.podcast')),
            ],
            options={
                'ordering': ('directory__ordering',),
                'unique_together': {('directory', 'podcast')},
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=30)),
                ('published', models.DateTimeField()),
                ('image', models.ImageField(blank=True, max_length=255, null=True, upload_to=pico.podcasts.models.Post.upload_image)),
                ('summary', models.TextField()),
                ('body', markdownx.models.MarkdownxField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to='podcasts.host')),
                ('categories', models.ManyToManyField(blank=True, related_name='blog_posts', to='podcasts.Category')),
                ('podcast', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to='podcasts.podcast')),
            ],
            options={
                'ordering': ('-published',),
                'unique_together': {('slug', 'podcast')},
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=30)),
                ('ordering', models.PositiveIntegerField(default=0)),
                ('image', models.ImageField(blank=True, max_length=255, null=True, upload_to=pico.podcasts.models.Page.upload_image)),
                ('body', markdownx.models.MarkdownxField(blank=True, null=True)),
                ('menu_visible', models.BooleanField(default=True, verbose_name='show in menu')),
                ('menu_title', models.CharField(blank=True, max_length=50, null=True, verbose_name='menu item title')),
                ('cta', models.BooleanField(verbose_name='highlight in menu')),
                ('podcast', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pages', to='podcasts.podcast')),
            ],
            options={
                'ordering': ('ordering',),
                'unique_together': {('slug', 'podcast')},
            },
        ),
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('guid', models.CharField(db_index=True, max_length=255)),
                ('published', models.DateTimeField()),
                ('number', models.CharField(db_index=True, max_length=3)),
                ('bonus', models.BooleanField(default=False)),
                ('trailer', models.BooleanField(default=False)),
                ('artwork', models.ImageField(blank=True, max_length=255, null=True, upload_to=pico.podcasts.models.Episode.upload_artwork)),
                ('summary', models.TextField()),
                ('feed_description', models.TextField()),
                ('enclosure_url', models.URLField(max_length=255, unique=True, verbose_name='enclosure URL')),
                ('body', markdownx.models.MarkdownxField(blank=True, null=True)),
                ('categories', models.ManyToManyField(blank=True, related_name='episodes', to='podcasts.Category')),
                ('hosts', models.ManyToManyField(related_name='episodes', to='podcasts.Host')),
                ('podcast', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='episodes', to='podcasts.podcast')),
                ('season', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='episodes', to='podcasts.season')),
            ],
            options={
                'ordering': ('-published',),
                'unique_together': {('guid', 'podcast')},
            },
        ),
    ]
