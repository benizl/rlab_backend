from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register

@dajaxice_register
def do_inputs(request, id, val):
	result = "%d is %s" % (id, str(val))
	dajax = Dajax()
	dajax.assign('#result', 'value', result)
	return dajax.json()
