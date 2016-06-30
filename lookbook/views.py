from django.shortcuts import render_to_response
from lookbook.models import Lookbook
from django.template import RequestContext
# Create your views here.
def get_published_lookbook(request):
	lookbook = ''
	try:
		lookbook = Lookbook.objects.get(is_published = True)
	except:
		pass
		
	return render_to_response('lookbook.html',{"lookbook":lookbook},context_instance = RequestContext(request) )