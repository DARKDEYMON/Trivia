from django.shortcuts import render,render_to_response
from django.template import RequestContext
from trivia.aplicaciones.sistema.forms import *
#from django.contrib.auth import login,logout,authenticate

# Create your views here.
def usuario_login_prinsipal(request):
	name="login"
	return render_to_response("principales/index_login.html",{"name":name,"login":form_usuario_for_final_user()},RequestContext(request))