from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register
import logging
import json

import hardware

log = logging.getLogger(__name__)

@dajaxice_register
def do_switches(request, state):
	hardware.switches(state)
	log.debug("Switches: %x", state)
	return json.dumps({'result' : 'ok'})

@dajaxice_register
def do_key(request, id, state):
	hardware.keys(id, state)
	log.debug("Keys: %x", state)
	return json.dumps({'result' : 'ok'})

@dajaxice_register
def do_reset(request):
	log.debug("resetting board")
	hardware.reset()
	return json.dumps({'result' : 'ok'})

@dajaxice_register
def do_demo(request):
	log.debug("loading demo")
	ret = hardware.load_demo()

	if ret:
		return json.dumps({'result' : ret})
	else:
		return json.dumps({'result' : 'ok'})
