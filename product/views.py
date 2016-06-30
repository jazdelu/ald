from django.shortcuts import render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from product.models import Product,Category
from django.template import RequestContext
from django.http import Http404

# Create your views here.

def get_products_by_category(request,slug):
	try:
		category = Category.objects.get(slug = slug)
	except:
		raise Http404

	product_list = Product.objects.filter(category = category)
	paginator = Paginator(product_list, 9)
	page = request.GET.get('page')
	try:
		products = paginator.page(page)
	except PageNotAnInteger:
		products = paginator.page(1)
	except EmptyPage:
		products = paginator.page(paginator.num_pages)

	return render_to_response('product.html',{ 'products':products,'category':category }, context_instance = RequestContext(request))