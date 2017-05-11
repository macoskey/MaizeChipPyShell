# "b" functions for MaizeChipPy
# com_number = number of virtual com port used
# MaizeChipPy 1.0 May 2017 JJM

import serial
import numpy as np
from initialize import open_serial_port
from math import floor
from math import ceil

startcode = 170
endcode = 85

def b_stop_execution:
	global ser
	open_serial_port()
	
	bdaddr = 0
	bcmd = 0
	data_send = np.array([startcode,bcmd,0,0,0,0,0,endcode,1,1,1,1,1,1,1,1],dtype='uint8')
	ser.write(data_send)
	return 0
	
def b_mask_off:
	global ser
	open_serial_port()
	
	bcmd = 13
	data_send = np.array([startcode,bcmd,0,255,255,255,255,endcode,1,1,1,1,1,1,1,1],dtype='uint8')
	ser.write(data_send)
	return 0
	
def b_select_motherboard(n):
	global ser
	open_serial_port()
	
	bcmd = 10
	data_send = np.array([startcode,bcmd,0,0,0,0,n % 256,endcode,1,1,1,1,1,1,1,1],dtype='uint8')
	ser.write(data_send)
	return 0
	
def b_set_chipmem_wloc(n):
	global ser
	open_serial_port()
	
	bcmd = 6
	data_send = np.array([startcode,bcmd,0,0,0,floor(n/256),n % 256,endcode,1,1,1,1,1,1,1,1],dtype='uint8')
	ser.write(data_send)
	return 0
	
def b_set_imem_wloc(n):
	global ser
	open_serial_port()
	
	bcmd = 4
	data_send = np.array([startcode,bcmd,0,0,0,floor(n/256),n % 256,endcode,1,1,1,1,1,1,1,1],dtype='uint8')
	return 0
	
	
	
# THESE NEED WORK
def b_set_mask(n):
	global ser
	open_serial_port()
	
	q_val = np.fliplr(n)
	bcmd = 13
	data_send = np.array([startcode,bcmd,0,dec
	
	ser.write(data_send)
	return 0
def b_single_channel_mask(n):
	global ser
	open_serial_port()
	ser.write(data_send)
	return 0
#################


def b_execute_program(n):
	global ser
	open_serial_port()
	
	bcmd = 1
	data_write = np.array([startcode,bcmd,0,0,0,floor(n/256),n % 256,endcode,1,1,1,1,1,1,1,1],dtype='uint8')
	
	ser.write(data_send)
	return 0
	
def b_write_chipmem(n):
	global ser
	open_serial_port()
	
	bcmd = 7
	data_write = np.array([startcode,bcmd,0,n[3],n[2],n[1],n[0],endcode,1,1,1,1,1,1,1,1],dtype='uint8')
	
	ser.write(data_send)
	return 0
	
def bgo:
	b_execute_program
	return 0
	
def bstop:
	b_stop_execution
	return 0
	



































