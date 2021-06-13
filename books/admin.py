from django.contrib import admin
from .models import *


class AuthorAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Name of the Author', {'fields': ['author_name', ]}),
        ('Biography (optional)', {'fields': ['biography', ]}),
    ]


class PublisherAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Publisher Details', {'fields': [
            'publisher_name', 'establish_date',
        ]}),
        ('Address', {'fields': ['address', ]}),
    ]


class BookAdmin(admin.ModelAdmin):
    fieldsets = [
        ('General Information', {'fields': [
            ('book_name', 'category',),
        ]}),
        ('Publishing Details', {'fields': [
            ('author', 'publisher',),
        ]}),
        ('Commercial Details', {'fields': [
            ('price', 'discount'),
            ('page_count', 'publication_date',),
            ('description'),
        ]}),
    ]


class RatingAdmin(admin.ModelAdmin):
    fields = [
        ('book', 'rating',),
        ('comment',),
    ]


admin.site.register(Author, AuthorAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Rating, RatingAdmin)
