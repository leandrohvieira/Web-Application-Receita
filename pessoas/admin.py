from django.contrib import admin
from.models import Pessoa

# Register your models here.
class listando_pessoas(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 5


admin.site.register(Pessoa, listando_pessoas)