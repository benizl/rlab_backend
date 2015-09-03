import serial, os
import logging

de2serial = None
ardserial = None

switchstate = '00000'
keystate = 'F'

log = logging.getLogger(__name__)

def _check_init():
	global de2serial, ardserial
	ardPath = None
	de2Path = None

	try:
		basepath = '/dev/serial/by-id'
		for p in os.listdir(basepath):
			if 'arduino' in p.lower():
				ardPath = os.path.join(basepath, p)
			elif 'prolific' in p.lower():
				de2Path = os.path.join(basepath, p)
	except OSError as e:
		print e
		log.exception("Can't scan serial ports")
		return

	if de2serial is None and de2Path is not None:
		try:
			de2serial = serial.Serial(de2Path, 115200)
		except:
			print("Can't open DE2 serial port")

	if ardserial is None and ardPath is not None:
		try:
			ardserial = serial.Serial(ardPath, 115200)
		except:
			print("Can't open Arduino serial port")

def _update_state():
	_check_init()

	if de2serial is None: return

	outstr = switchstate + keystate + '\n'
	de2serial.write(outstr)
	log.debug("New state %s" % outstr)

def switches(swstate):
	global switchstate
	n = 0
	for i in range(18,0,-1):
		n <<= 1
		if swstate[str(i)]: n += 1

	assert n >= 0 and n <= 0xFFFFF

	switchstate = format(n, '05x')
	_update_state()

def keys(id, state):
	global keystate
	n = int(keystate, 16)

	# Keys are active-low
	if not state:
		n |= 1 << (id - 1)
	else:
		n &= ~(1 << (id - 1))

	keystate = format(n, 'x')

	_update_state()

def load_bitstream(bsfname):
	import subprocess

	log.info("New bitstream %s", bsfname)
	print bsfname
	# It'd be nice to just use $PATH but that's nontrivial to set up properly
	# from systemd init files?
	subprocess.call(['/home/vlabadmin/altera/11.1sp2/quartus/bin/quartus_pgm', '-m', 'jtag', '-o', 'p;%s' % bsfname])

def load_demo():
	return load_bitstream('/opt/rlab_demo/demo.sof')

def reset():
	_check_init()

	if ardserial is None: return
	log.debug("Restting board")
	ardserial.write('reset\n')
