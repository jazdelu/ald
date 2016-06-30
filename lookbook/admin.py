from django.contrib import admin
from lookbook.models import *
# Register your models here.
class LookbookAdmin(admin.ModelAdmin):
	list_display = ('name','is_published')

admin.site.register(Lookbook, LookbookAdmin)

class ImageAdmin(admin.ModelAdmin):
	list_display = ('image','lookbook')
	list_filter = ('lookbook',)
admin.site.register(Image,ImageAdmin)