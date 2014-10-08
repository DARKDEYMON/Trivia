from models import *
from django.forms import *
#from django import forms, PasswordInput

class form_usuario_for_admin(ModelForm):
	class Meta:
		widgets = {
        	'password': PasswordInput(),
        }
class form_usuario_for_final_user(ModelForm):
	class Meta:
		model=usuario
		fields = ['username','password','imagen','correo']
		widgets = {
        	'password': PasswordInput(),
        }