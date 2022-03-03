from django.contrib import admin

from .models import Quote

@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'quote',
        'no_of_letters',
        'no_of_vowels',
        'no_of_consonants',
        'avg_len_of_words',
        'three_longest_words'
    ]
    ordering = ['-id']
