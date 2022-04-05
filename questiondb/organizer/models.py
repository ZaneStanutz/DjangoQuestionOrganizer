from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=31, unique=True)
	slug = models.SlugField(max_length=31, unique=True, help_text='A label for URL config.')
	def __str__(self):
		return self.name.title()
	class Meta:
		ordering = ['name'] 
	def get_absolute_url(self):
		return reverse('organizer_category_detail',
				 kwargs={'slug' : self.slug})

class Question(models.Model):
	name = models.CharField(max_length=31)
	slug =  models.SlugField()
	question = models.TextField()
	categories = models.ManyToManyField(Category)
	def __str__(self):
		return self.question
	class Meta:
		ordering = ['name'] 
