"""ald URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from page import views as page_views
from product import views as product_views
from lookbook import views as lookbook_views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', page_views.homepage, name = 'homepage'),
    url(r'^category/(?P<slug>[\w-]+)/$', product_views.get_products_by_category, name = 'get products by category'),
    url(r'^p/(?P<slug>[\w-]+)/$', page_views.get_page_by_slug, name = 'get page by slug'),
    url(r'^lookbook/$', lookbook_views.get_published_lookbook, name = 'get_published_lookbook'),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
