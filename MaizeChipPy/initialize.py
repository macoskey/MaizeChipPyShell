# Initializes USB communications with FPGA
# com_number = number of virtual com port used
# MaizeChipPy 1.0 May 2017 JJM

import time
import serial

def maize_init(com_number):
	
	# define the serial port as a global variable
	global ser 
	global port
	
	print " Initializing with COM port %s...\n" % com_number
	port = "COM%s" % com_number
	try:
		ser = serial.Serial(port)
		print "Communications successfully initialized on "
		print ser.name
		print "\n"
		break
	except:
		print "An error has occured... restart everything\n"
			
	
	

