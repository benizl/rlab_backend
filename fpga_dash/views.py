from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404, HttpResponseServerError
from django.views.decorators.http import require_POST

import random, string
viewid = ''.join([random.choice(string.ascii_letters) for x in range(16)])

def index(request):
	return render(request, 'dashboard/index.html', {'viewid' : viewid})

def linkage(request):
	return render(request, 'dashboard/linkage.html', {'viewid' : viewid})

@require_POST
def ul_bitstream(request):
	import tempfile
	fobj = request.FILES['bs-upload']
	tmp = tempfile.NamedTemporaryFile()

	for chunk in fobj.chunks:
		tmp.write(chunk)

	ret = hardware.load_bitstream(tmp.name)

	if ret:
		return HttpResponseServerError()
	else:
		return HttpResponse('')

@require_POST
def ul_audio(request):
	print "TODO: Play music"
	print requiest.FILES['audio-upload']
	return HttpResponse('')