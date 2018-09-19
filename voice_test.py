#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import os.path
import sys
import argparse
from osc4py3.as_eventloop import *
from osc4py3 import oscbuildparse
from mutagen.mp3 import MP3 as mp3
import pygame
import requests
from time import sleep

#read .pmdl File
dir = os.path.dirname(os.path.abspath(__file__))

#You say "Hey, FOX".
HOTWORD_FILE = dir + "voice/FOX.pmdl"

#再生したいmp3ファイル
filename1 = 'voice/intro.mp3'
filename2 = 'voice/face_expression.mp3'
filename3 = 'voice/hand_sign.mp3'
filename4 = 'voice/wait.mp3'


#osc setup
osc_startup()
osc_udp_client("127.0.0.1", 12345, "client")
osc_udp_server("127.0.0.1", 56789, "server")

#OSC state send
def make_osc(state):
    msg = osc_message_builder.OscMessageBuilder(address= "/event_state")
    msg.add_arg(state)
    msg = msg.build()

    return msg

#callback function
def handlerfunction(msg_receive):
    osc_receive = msg_receive

#mixer setting
pygame.mixer.init()
#osc receive
osc_receive = 0

finished = False
while not finished:
#0
    state = 0
    msg = oscbuildparse.OSCMessage("/event_state", None, [state])
    osc_send(msg, "client")
    osc_process()
    
#1
    osc_method("/state_receive", handlerfunction)
    osc_process()
    state = osc_receive

    pygame.mixer.music.load(filename1)
    mp3_length = mp3(filename1).info.length
    pygame.mixer.music.play(1)
    sleep(mp3_length + 0.25)
    pygame.mixer.music.stop()

    msg = oscbuildparse.OSCMessage("/event_state", None, [state])
    osc_send(msg, "client")
    osc_process()

#2
    osc_method("/state_receive", handlerfunction)
    osc_process()
    state = osc_receive

    pygame.mixer.music.load(filename2)
    mp3_length = mp3(filename2).info.length
    pygame.mixer.music.play(1)
    sleep(mp3_length + 0.25)
    pygame.mixer.music.stop()

    msg = oscbuildparse.OSCMessage("/event_state", None, [state])
    osc_send(msg, "client")
    osc_process()

#3
    osc_method("/state_receive", handlerfunction)
    osc_process()
    state = osc_receive

    pygame.mixer.music.load(filename3)
    mp3_length = mp3(filename3).info.length
    pygame.mixer.music.play(1)
    sleep(mp3_length + 0.25)
    pygame.mixer.music.stop()

    msg = oscbuildparse.OSCMessage("/event_state", None, [state])
    osc_send(msg, "client")
    osc_process()

#4
    osc_method("/state_receive", handlerfunction)
    osc_process()
    state = osc_receive

    pygame.mixer.music.load(filename4)
    mp3_length = mp3(filename4).info.length
    pygame.mixer.music.play(1)
    sleep(mp3_length + 0.25)
    pygame.mixer.music.stop()

    msg = oscbuildparse.OSCMessage("/event_state", None, [state])
    osc_send(msg, "client")
    osc_process()

    finished = True

osc_terminate()
