# "a" functions for MaizeChipPy
# com_number = number of virtual com port used
# MaizeChipPy 1.0 May 2017 JJM

import serial
import numpy as np

# pre-defined parameters
startcode = 170;
endcode = 85;
bcmd = 5;
acmd = 3;

	
def a_fire(n):
	global ser
	try:
		ser.open()
		break
	except:
		# port already open
	ser.reset_output_buffr()
	
	data = np.array([0, 0, 0, n, 8])
	ser.write(data)
	
	return 0
	
def a_halt(n):
	
	return 0
	
def a_loadincr_chipmem(n):
	
	return 0
	
def a_set_amp(n):
	
	return 0
	
def a_set_LEDs(n):
	
	return 0
	
def a_set_phase(n):
	
	return 0
	
def a_set_trig(n):
	
	return 0
	
def a_start_loop(n):
	
	return 0
	
def a_end_loop(n):
	global ser
	ser.open()
	ser.reset_output_buffer()
	
	seq = dec
	byte_str = join()
	byte1 = int(byte_str
	return 0	
	
def a_wait(n):
	
	return 0
	
def a_waitsetc(n):
	
	return 0

