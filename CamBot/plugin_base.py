#!/usr/bin/python                                                               
# encoding: utf-8                                                               
"""                                                                             
Created by ad on 2009-02-16.                                                    
NoCopyright 2009 __18kpies__. No rights reserved.                               
"""

import string
import servo
import serial
import time
import random

import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks


class CamBot(callbacks.Plugin):
    """Add the help for "@plugin help CamBot" here
    This should describe *how* to use this plugin."""
    threaded = True

#    def camMove(self, irc, msg, args, words):
def camMove(self, irc, msg, servo, angle):
	"""<value in degrees>

	Moves the camera accordingly
	"""
	motor = 1   #string.atoi(words[0])
	angle = string.atoi(words[0])
		
	if (0 <= angle <= 180):
		#print motor
		ser = serial.Serial('/dev/tty.usbserial-A9005aX1', 9600, timeout=1) # instanciate serial
		ser.open() # opens serial port
		ser.write(chr(255))
		ser.write(chr(motor))
		ser.write(chr(angle))
		response = ser.readline() # reads the serial buffer
		#print response
		ser.close()
	else:
		#print "Servo angle must be an integer between 0 and 180.\n"

		camMove(servo.move(1, int(angle)))

		irc.reply("Moving Servo %i %i degrees" % (motor, angle))

		camMove = wrap(camMove, [many('something')])

Class = CamBot

# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79: