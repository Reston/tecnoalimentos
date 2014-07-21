from django.conf.urls import patterns, url

urlpatterns = patterns(
	'tecnoalimentos.apps.homepage.views',
	url(r'^$', 'index', name="homepageindex"),
	url(r'^quienessomos/$', 'aboutus', name="homepageaboutus"),
	url(r'^contacto/$', 'contact', name="homapagecontact"),
	url(r'^productosysoluciones/$', 'products', name="homepageproducts"),
)
