from django.contrib import admin
from product.models import Category, Color, Product, Image
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name','slug')

admin.site.register(Category, CategoryAdmin)

class ImageInline(admin.TabularInline):
	model = Image
	extra = 1

class ProductAdmin(admin.ModelAdmin):
	list_display = ('serial', 'name', 'category','pub_date')
	inlines = [ImageInline,]
	filter_horizontal = ('color',)

class ColorAdmin(admin.ModelAdmin):
	list_display = ('color','name')

admin.site.register(Product, ProductAdmin)
admin.site.register(Color,ColorAdmin)
