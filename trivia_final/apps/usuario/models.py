from django.db import models
from thumbs import ImageWithThumbsField
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
# Create your models here.

class datos_adicionales_usuario(models.Model):
	username=models.OneToOneField(User, unique=True)
	pais=models.CharField(max_length=100, null=True)
	avatar=ImageWithThumbsField(upload_to="avatares/", sizes=((50,50),(200,200)), null=True)
	def __unicode__(self):
		return self.username.username
	class Meta:
		verbose_name = _('Datos Adicionales de usuario')
		verbose_name_plural = _('Datos Adicionales de usuarios')