from django.db import models

# Create your models here.

class usuario(models.Model):
	username = models.CharField(max_length=100, unique=True)
	password = models.CharField(max_length=100)
	imagen = models.ImageField(upload_to='fotos/',blank=True)
	correo = models.EmailField(max_length=70,blank=True)
	def __unicode__(self):
		return "-->"+self.username