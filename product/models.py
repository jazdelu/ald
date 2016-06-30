from __future__ import unicode_literals

from django.db import models
from colorful.fields import RGBColorField

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length = 128, verbose_name = 'Name')
	slug = models.SlugField(max_length = 128, verbose_name = 'Slug')
	banner = models.ImageField(upload_to = 'banner/',verbose_name = 'Banner')

	class Meta:
		verbose_name = 'Category'
		verbose_name_plural = 'Category'

	def __unicode__(self):
		return self.name

class Color(models.Model):
	name = models.CharField(max_length = 128, verbose_name='Name')
	color = RGBColorField()

	class Meta:
		verbose_name = 'Color'
		verbose_name_plural = 'Color'

	def __unicode__(self):
		return self.name

class Product(models.Model):
	name = models.CharField(max_length=128, verbose_name = 'Name')
	serial = models.CharField(max_length = 128,verbose_name = 'Serial',blank = True,null = True)
	short_description = models.CharField(max_length = 128,verbose_name = 'Short Description')
	category = models.ForeignKey('product.Category',related_name = 'products')
	color = models.ManyToManyField(Color)
	pub_date = models.DateTimeField(verbose_name = "Publish Date", auto_now_add = True)
	last_modified = models.DateTimeField(auto_now = True)

	class Meta:
		verbose_name = 'Product'
		verbose_name_plural = 'Product'
		ordering =['-pub_date']

class Image(models.Model):
	product = models.ForeignKey(Product,related_name = "images")
	image = models.ImageField(upload_to='product/',verbose_name = 'Image')
	order = models.IntegerField(verbose_name = 'Image display order', default = 1)
	class Meta:
		verbose_name = 'Image'
		verbose_name_plural = 'Image'
		ordering = ['order',]

	def __unicode__(self):
		return self.image.url