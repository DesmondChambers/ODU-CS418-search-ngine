from django.contrib import admin
from .models import Search, Searchsave, History

# Register your models here.

class SearchAdmin(admin.ModelAdmin):
    list_display = ('contributor_author', 'description_abstract', 'identifier_uri', 'slug')

admin.site.register(Search, SearchAdmin)

admin.site.register(Searchsave)

admin.site.register(History)

