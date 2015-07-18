from django.shortcuts import redirect

def redirect_to_dash(request):
	return redirect('dashboard/')
