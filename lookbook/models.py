from django.db import models
# Create your models here.
class Lookbook(models.Model):
	name = models.CharField(max_length = 128)
	pub_date = models.DateTimeField(verbose_name = 'Publish Date', auto_now_add = True)
	is_published = models.BooleanField(verbose_name = 'Publish this lookbook?', default = False)

	class Meta:
		verbose_name = 'Lookbook'
		verbose_name_plural = 'Lookbooks'
		ordering = ['-pub_date']

	def __unicode__(self):
		return self.name

	def save(self, *args, **kwargs):
		if self.is_published:
			try:
				lookbook = Lookbook.objects.get(is_published = True)
				lookbook.is_published = False
				lookbook.save()
			except:
				pass
		super(Lookbook,self).save(*args, **kwargs)

class Image(models.Model):
	lookbook = models.ForeignKey(Lookbook, related_name = 'images')
	image = models.ImageField(upload_to = 'lookbook/', verbose_name = 'Image', help_text = 'Image size should be smaller than 700KB')
	pub_date = models.DateTimeField(verbose_name = 'Publish Date', auto_now_add = True)

	class Meta:
		verbose_name = 'Image'
		verbose_name_plural = 'Images'
		ordering = ['-pub_date']

	def __unicode__(self):
		return self.image.url