from page.models import Page

def get_pages_in_nav(request):
	page_list = Page.objects.all()
	return {'pages':page_list}