from django.shortcuts import redirect

def redirect_to_dash(request):
	rd = redirect('dashboard/')
	rd['Location'] += '?' + request.META['QUERY_STRING']
	return rd
