from django.db import models

#class Conversation(models.Model):
#	pass

#class Response(models.Model):
#    text = models.TextField(defualt = '')

class Sentence(models.Model):
	text = models.TextField(default ='')
	#conversation = models.ForeignKey(Conversation,default=None)
# Create your models here.
