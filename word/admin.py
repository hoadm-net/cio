from django.contrib import admin
from .models import Adverb, Word


class ModelAdverb(admin.ModelAdmin):
    list_display = ('txt', 'lvl', )
    search_fields = ('txt', )
    list_filter = ('lvl', )
    ordering = ('txt', )


class ModelWord(admin.ModelAdmin):
    list_display = ('txt', 'sentiment', 'score', )
    search_fields = ('txt',)
    list_filter = ('sentiment',)
    ordering = ('txt',)


admin.site.register(Adverb, ModelAdverb)
admin.site.register(Word, ModelWord)
