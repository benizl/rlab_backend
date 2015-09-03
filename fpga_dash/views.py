from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404, HttpResponseServerError
from django.views.decorators.http import require_POST

import hardware

import random, string
viewid = ''.join([random.choice(string.ascii_letters) for x in range(16)])

def index(request):
	return render(request, 'dashboard/index.html', {'viewid' : viewid})

def linkage(request):
	return render(request, 'dashboard/linkage.html', {'viewid' : viewid})

@require_POST
def ul_bitstream(request):
	fobj = request.FILES['bs-upload']
	print fobj

	tmp = open('/tmp/tmp.sof', 'w')
	for chunk in fobj.chunks():
		tmp.write(chunk)

	tmp.close()
	ret = hardware.load_bitstream('/tmp/tmp.sof')

	print ret
	if ret:
		return HttpResponseServerError()
	else:
		return HttpResponse('')

@require_POST
def ul_audio(request):
	print "TODO: Play music"
	print request.FILES['audio-upload']
	return HttpResponse('')
