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
	to artbus stepper comands, which are then sent 
	via serial connection."""

	def __init__(self, irc):
		self.__parent = super(StepperBot, self)
		self.__parent.__init__(irc)
    
#self.TESTF = False 

	#servo patterns for X and Y axis:
	
west_pattern = servo.move(2,45)
east_pattern = servo.move(2,90)
deepwest_pattern = servo.move(2,180)
deepeast_pattern = servo.move(2,0)
artic_pattern = servo.move(2,45)
antartic_pattern = servo.move(2,90)
deepnorth_pattern = servo.move(2,180)
deepsouth_pattern = servo.move(2,0)
        		
	# map irc commands to patterns
self.irc_patterns = {"west" : west_pattern, "east" : east_pattern, "deepwest" : deepwest_pattern, "deepeast" : deepeast_pattern, "artic" : artic_pattern, "antartic" : antartic_pattern, "deepnorth" : deepnorth_pattern, "deepsouth" : deepsouth_pattern}
self.reset_pattern = (0,0)		
	# serial config
if self.TESTF == False:
    self.ser = serial.Serial() # instanciate serial class as ser
    self.ser.port = '/dev/tty.usbserial-A9005aX1' #  connection device
    self.ser.baudrate = 9600 # sets the speed
    self.ser.timeout = 0.1 # to not occupy the line forever
else:
    self.single_cmd_break = 0	# break between each artbus_command
            
	   # DO COMMAND (!west, !east etc.)
    def DoCommand(self, irc, direction):
        """takes no arguments
        Translates irc command to artbus command."""
			
	# get patterns
        patterns = self.irc_patterns[direction]
		#irc.reply("received direction command: " + direction)
		#irc.reply("move cam "+direction+"...")		
		
		# open serial connection
        self.ser.open() # opens serial port
	
	# ACA VOY	
	ser = serial.Serial('/dev/tty.usbserial', 9600)
	ser.write('5')

    pass

Class = StepperBot