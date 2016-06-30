from django.contrib import admin
from page.models import Homepage, HomepageLink, Page, Section
from page.forms import PageForm, HomepageLinkForm
# Register your models here.

class HomepageLinkInline(admin.StackedInline):
	model = HomepageLink
	extra = 1
	min_num = 2
	form = HomepageLinkForm

class HomepageAdmin(admin.ModelAdmin):
	list_display = ('title',)
	inlines = [HomepageLinkInline,]

admin.site.register(Homepage, HomepageAdmin)

class SectionInline(admin.StackedInline):
	model = Section
	extra = 1
	form = PageForm

class PageAdmin(admin.ModelAdmin):
	list_display = ('title','slug','order',)
	inlines = [SectionInline,]
	form = PageForm

admin.site.register(Page, PageAdmin)