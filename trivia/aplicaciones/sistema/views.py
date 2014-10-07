from django.shortcuts import render,render_to_response
from django.template import RequestContext
from trivia.aplicaciones.sistema.forms import *

# Create your views here.
def usuario_login(request):
	name="login"
	return render_to_response("principales/index_login.html",{"name":name,"login":form_usuario_for_final_user()},RequestContext(request))