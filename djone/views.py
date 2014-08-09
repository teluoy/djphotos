#coding:utf-8
from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from djone.models import One
from .forms import *

def index(request):
	profile = One.objects.all()
	d = {'p':profile}
	d['form']=OneForm()
	if request.method == "POST":
		p = OneForm(request.POST,request.FILES)
		if p.is_valid():
			p.save()
		else:
			d['form']=p
			return render_to_response('index.html', d, context_instance=RequestContext(request))


	return render_to_response('index.html', d, context_instance=RequestContext(request))
'''
def indexph(request):

	if request.method == "POST":
		p = OneForm(request.POST,request.FILES)
		if p.is_valid():
			p.save()
	return redirect('/')
'''
