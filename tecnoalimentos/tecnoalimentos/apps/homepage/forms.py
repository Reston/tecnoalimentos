#!/usr/local/bin/python
# -*- encoding: utf-8 -*-
from django import forms


class contactForm(forms.Form):
	nombre = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Su nombre'}))
	pais = forms.CharField(widget=forms.TextInput(attrs={'placeholder': u'Ubicación de la empresa'}))
	email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'nick@email.com'}))
	empresa = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Empresa donde trabaja'}))
	telefono = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '58-999-9999999', 'type': 'tel'}))
	texto = forms.CharField(widget=forms.Textarea)

	def clean_asunto(self):
		cd = self.cleaned_data
		asunto = cd.get('asunto')
		if len(asunto) < 3:
			raise forms.ValidationError("El asunto debe tener mas de 2 letras")
		return asunto

	def clean_texto(self):
		cd = self.cleaned_data
		texto = cd.get('texto')
		if len(texto) < 4:
			raise forms.ValidationError("*")
		return texto
