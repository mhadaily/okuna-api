from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

# Register your models here.
from openbook_common.models import Emoji, EmojiGroup, Badge, ProxyWhitelistDomain


class EmojiGroupEmoji(admin.TabularInline):
    model = Emoji


class EmojiGroupAdmin(TranslationAdmin):
    inlines = [
        EmojiGroupEmoji
    ]

    list_display = (
        'id',
        'keyword',
        'created',
        'color',
        'order'
    )


admin.site.register(EmojiGroup, EmojiGroupAdmin)


class EmojiAdmin(TranslationAdmin):
    pass


admin.site.register(Emoji, EmojiAdmin)


class BadgeAdmin(TranslationAdmin):
    pass


admin.site.register(Badge, BadgeAdmin)


class ProxyWhitelistDomainAdmin(admin.ModelAdmin):
    list_display = (
        'domain',
    )


admin.site.register(ProxyWhitelistDomain, ProxyWhitelistDomainAdmin)
