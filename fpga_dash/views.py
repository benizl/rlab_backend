from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views.decorators.http import require_POST

import uuid
viewid = str(uuid.uuid1())

def index(request):
	return render(request, 'dashboard/index.html', {'viewid' : viewid})

def linkage(request):
	return render(request, 'dashboard/linkage.html', {'viewid' : viewid})

@require_POST
def ul_bitstream(request):
	print "TODO: Load bitstream"
	print request.FILES['bs-upload']
	return HttpResponse('')

@require_POST
def ul_audio(request):
	print "TODO: Play music"
	print requiest.FILES['audio-upload']
	return HttpResponse('')