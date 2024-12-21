from django.contrib import admin
from .models import Artist, Museum, Painting

class ArtistAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'birth_date')
    search_fields = ['name', 'surname']

class MuseumAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'city', 'country')
    list_filter = ('city', 'country')
    search_fields = ['name', 'city', 'country']

class PaintingAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'creating_year', 'artist', 'museum')
    list_filter = ('artist', 'museum')
    search_fields = ['name']

admin.site.register(Artist, ArtistAdmin)
admin.site.register(Museum, MuseumAdmin)
admin.site.register(Painting, PaintingAdmin)
