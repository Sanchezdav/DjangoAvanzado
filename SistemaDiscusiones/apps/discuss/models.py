from django.db import models
from apps.users.models import User

class TimeStampModel(models.Model):

	user = models.ForeignKey(User, db_index=True)
	description = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	class Meta:
		abstract = True

class Tag(models.Model):

	nombre = models.CharField(max_length=10)

	def __unicode__(self):
		return self.nombre

class Question(TimeStampModel):

	tag = models.ManyToManyField(Tag)
	title = models.CharField(max_length=200)

	def __unicode__(self):
		return '%s %s' % (self.user, self.title)

class Answer(TimeStampModel):

	def __unicode__(self):
		return self.user
