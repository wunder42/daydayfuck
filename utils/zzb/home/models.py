from django.db import models

from model_utils.models import TimeStampedModel
# Create your models here.

class Gititem(TimeStampedModel):

	itemid = models.CharField(max_length=20, unique=True, verbose_name='item primar id')
	title = models.CharField(max_length=20, verbose_name='title')
	subtitle = models.CharField(max_length=20, verbose_name='subtitle')
	maintext = models.CharField(max_length=2000, verbose_name='maintext')
	giturl = models.URLField(max_length=100, verbose_name='git url address')

	class Meta:
		verbose_name = u'git item'
		verbose_name_plural = u'git item'

	def __unicode__(self):
		return '%s' % self.title
