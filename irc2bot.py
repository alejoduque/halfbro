###
# No Copyright 2009 alejoduque based on code from favian vogeli for the ArtBus
# No rights reserved.
###

import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks

import serial #import serial library
import sys, time
import servo #import servo library

class StepperBot(callbacks.Plugin):
	"""translates irc commands like right, left, up, down 
	to artbus stepper comands or servos on arduinos, to be sent 
	via serial connection."""
	
	def __init__(self, irc):
		self.__parent = super(StepperBot, self)
		self.__parent.__init__(irc)
		
		# flag to set if script shall run as test-only without serial connection or live with serial connection
		self.TESTF = False 
		
        #servo patterns for X axis:
		
		west_pattern = servo.move(2,45)
		east_pattern = servo.move(2,90)
		deepwest_pattern = servo.move(2,180)
		deepeast_pattern = servo.move(2,0)

        # servo pattern for Y axis:
		artic_pattern = servo.move(2,45)
		antardic_pattern = servo.move(2,90)
		deepnorth_pattern = servo.move(2,180)
		deepsouth_pattern = servo.move(2,0)
		
		# map irc commands to patterns
		self.irc_patterns = {"west" : west_pattern, "east" : east_pattern, "deepwest" : deepwest_pattern, "deepeast" : deepeast_pattern, "artic" : artic_pattern, "antartic" : antartic_pattern, "deepnorth" : deepnorth_pattern, "deepsouth" : deepsouth_pattern}
		
		# serial config
		if self.TESTF == False:
			self.ser = serial.Serial() # instanciate serial class as ser
			self.ser.port = '/dev/tty.usbserial-A9005aX1' #  connection device
			self.ser.baudrate = 9600 # sets the speed
			self.ser.timeout = 0.01 # to not occupy the line forever
			
"""
HASTA ACA LAS COSAS ESTAN RELATIVAMENTE CLARAS, LUEGO DEBERA VENIR EL WRITE!	
"""	
	
	# DO COMMAND (!west, !east etc.)
	def DoCommand(self, irc, direction):
		
		# get patterns
		patterns = self.irc_patterns[direction]
		#irc.reply("received direction command: " + direction)
		#irc.reply("move cam "+direction+"...")
		
		
		# open serial connection
		if self.TESTF == False:
			try:
				self.ser.open() # opens serial port
			except serial.SerialException, e:
				print e # prints an error if it doesn't work
				irc.error("error: couldn't open serial connection")
		



Class = StepperBot
