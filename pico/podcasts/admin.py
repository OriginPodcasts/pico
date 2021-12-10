from django.contrib import admin
from .models import (
    Directory, SubscriptionLink,
    Podcast, Season, Host, Episode,
    Post, Page, Category
)


@admin.register(Directory)
class DirectoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Host)
class HostAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {
        'slug': ('name',)
    }

    filter_horizontal = ('podcasts',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {
        'slug': ('name',)
    }


class SeasonInline(admin.TabularInline):
    model = Season
    extra = 0


class SubscriptionLinkInline(admin.TabularInline):
    model = SubscriptionLink
    extra = 0


@admin.register(Podcast)
class PodcastAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'domain')
    prepopulated_fields = {
        'slug': ('name',)
    }

    inlines = (SeasonInline, SubscriptionLinkInline)
    fieldsets = (
        (
            None,
            {
                'fields': (
                    'name',
                    'short_name',
                    'slug',
                    'domain',
                    'rss_feed_url'
                )
            }
        ),
        (
            'Artwork and description',
            {
                'fields': (
                    'artwork',
                    'subtitle',
                    'description',
                    'about_page'
                )
            }
        ),
        (
            'Social media',
            {
                'fields': (
                    'twitter_username',
                    'facebook_username',
                    'instagram_username'
                ),
                'classes': ('collapse',),
            }
        ),
        (
            'Colours',
            {
                'fields': (
                    'colour_brand',
                    'colour_white',
                    'colour_dark',
                    'colour_text',
                    'colour_grey',
                    'colour_error',
                    'colour_success',
                    'colour_border',
                    'bg_colour',
                    'bg_grey'
                ),
                'classes': ('collapse',),
            }
        )
    )


@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'podcast',
        'published',
        'season',
        'number',
        'bonus',
        'trailer'
    )

    list_filter = ('podcast',)
    date_hierarchy = 'published'
    filter_horizontal = ('categories', 'hosts')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'podcast',
        'published'
    )

    list_filter = ('podcast',)
    date_hierarchy = 'published'
    prepopulated_fields = {
        'slug': ('title',)
    }

    filter_horizontal = ('categories',)


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'podcast',
        'menu_visible'
    )

    list_filter = ('podcast',)
    prepopulated_fields = {
        'slug': ('title',)
    }
