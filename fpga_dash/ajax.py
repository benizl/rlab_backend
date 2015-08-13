from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register

import json

#import hardware

@dajaxice_register
def do_switches(request, state):
#	hardware.switches(state)
	return json.dumps({'result' : 'ok'})

@dajaxice_register
def do_key(request, id, state):
	print id, state #"key %d in state %d" % (int(id), int(state))
	return json.dumps({'result' : 'ok'})

@dajaxice_register
def do_reset(request):
	print "resetting board"
	return json.dumps({'result' : 'ok'})

@dajaxice_register
def do_demo(request):
	print "loading demo"
	return json.dumps({'result' : 'ok'})
