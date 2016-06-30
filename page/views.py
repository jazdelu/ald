from django.shortcuts import render_to_response
from django.http import Http404
from page.models import Page, Homepage
from django.http import HttpResponse
from django.template import RequestContext

# Create your views here.
def get_page_by_slug(request,slug):
	page = ''
	try:
		page = Page.objects.get(slug = slug)
	except:
		raise Http404

	if page.slug == 'contact':
		template = 'contact.html'
	elif page.slug == 'services':
		template = 'services.html'
	elif page.slug == 'info':
		template = 'info.html'
	elif page.slug == 'about-us':
		template = 'about.html'


	return render_to_response(template,{"page":page},context_instance = RequestContext(request) )


def homepage(request):
	try:
		homepage = Homepage.objects.all()
	except:
		pass
	if not homepage:
		return HttpResponse("You haven't set a homepage, please login to admin interface to make some settings.")

	return render_to_response("index.html",{"homepage":homepage[0]},context_instance = RequestContext(request))