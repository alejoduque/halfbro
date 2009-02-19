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
    def move(self, irc, msg, args, motor, angle):
        """<motor> <value in degrees>

        Moves the camera accordingly
        """
        servo.move(motor, angle)
        irc.reply("Moving Servo %s %s degrees" % (motor, angle))
    move = wrap(move, ['int', 'int'])

Class = CamBot

# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
