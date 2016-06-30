from __future__ import unicode_literals

from django.db import models
from product.models import Category
# Create your models here.
class Homepage(models.Model):
	title = models.CharField(max_length = 128,verbose_name = 'Title', default = 'Homepage')
	banner = models.ImageField(upload_to = 'banner/', verbose_name = "Banner")

	class Meta:
		verbose_name = "Homepage Settings"
		verbose_name_plural = 'Homepage Settings'

	def __unicode__(self):
		return self.title

class HomepageLink(models.Model):
	page = models.ForeignKey('Homepage', related_name = 'links')
	title = models.CharField(max_length = 128, verbose_name = "title")
	image = models.ImageField(upload_to = 'link/', verbose_name = 'Image', help_text = 'Recommended size: 720px*720px, smaller than 300KB.')
	category  = models.ForeignKey(Category)
	order = models.IntegerField(help_text='The display order of links(icons) on homepage')

	class Meta:
		verbose_name = "Homepage Link"
		verbose_name_plural = "Homepage Links"
		ordering = ['order',]

	def __unicode__(self):
		return self.title

class Page(models.Model):
	title = models.CharField(max_length = 128,verbose_name = 'Title')
	slug = models.SlugField(max_length = 128, help_text = 'The strings display in page URL')
	banner = models.ImageField(upload_to = 'banner/', verbose_name = "Banner")
	order = models.IntegerField(verbose_name = 'Order', default = 1 ,help_text = 'The order of the menu in header and footer')
	content = models.TextField(verbose_name = "Content",  null = True, blank = True, help_text = 'Only available on CONTACT page')
	class Meta:
		verbose_name = 'Page'
		verbose_name_plural = 'Pages'
		ordering = ['order']

	def __unicode__(self):
		return self.title

class Section(models.Model):
	page = models.ForeignKey('Page',related_name = 'sections')
	title = models.CharField(max_length = 128,verbose_name = 'Title')
	image = models.ImageField(upload_to = 'section/',verbose_name = 'Image')
	content = models.TextField(verbose_name = "Content")

	class Meta:
		verbose_name = 'Section'
		verbose_name_plural = 'Sections'

	def __unicode__(self):
		return self.title