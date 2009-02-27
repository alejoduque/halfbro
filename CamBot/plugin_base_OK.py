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
    def move(self, irc, msg, args, angle):
        """<value in degrees>

        Moves the camera accordingly
        """
        irc.reply("Moving Servo 1 %s degrees" % angle)
    move = wrap(move, ['chr(int)'])

Class = CamBot

# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79: