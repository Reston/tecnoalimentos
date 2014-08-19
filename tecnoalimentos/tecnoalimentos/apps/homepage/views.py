#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from tecnoalimentos.apps.homepage.forms import contactForm
from django.template import RequestContext
from django.core.mail import send_mail


def index(request):
	return render_to_response('homepage/index.html', context_instance=RequestContext(request))


def aboutus(request):
	mision = "misión de la empresa"
	vision = "visión de la empresa"
	ctx = {'mision': mision, 'vision': vision}
	return render_to_response('homepage/quienesomos.html', ctx, context_instance=RequestContext(request))


def products(request):
	serv = "El arte de servir"
	ctx = {'serv': serv}
	return render_to_response('homepage/products.html', ctx, context_instance=RequestContext(request))


def contact(request):
	success = False
	if request.method == 'POST':
		form = contactForm(request.POST)
		if form.is_valid():
			success = True
			cd = form.cleaned_data
			asunto = u'Por: %s mail: %s ' % (cd['nombre'], cd['email'])
			content = u'Email contacto: %s \nAsunto: %s \nTelefono: %s \nDescripcion: %s' % (cd['email'], asunto, cd['telefono'], cd['texto'])
			print content
			#send_mail(asunto, content, cd['email'], ['info@duranjo.com'])
	else:
		form = contactForm()
	ctx = {'form': form, 'success': success}
	return render_to_response('homepage/contacto.html', ctx, context_instance=RequestContext(request))
