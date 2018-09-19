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

#OSC state send
def make_osc(state):
    msg = osc_message_builder.OscMessageBuilder(address= "/event_state")
    msg.add_arg(state)
    msg = msg.build()

    return msg

#callback function
def handlerfunction(msg_receive):
    osc_receive = msg_receive

def play_voice(filename):
    pygame.mixer.music.load(filename)
    mp3_length = mp3(filename).info.length
    pygame.mixer.music.play(1)
    sleep(mp3_length + 0.25)
    pygame.mixer.music.stop()


osc_startup()
osc_udp_server("127.0.0.1", 12345, "state_receive")
osc_udp_client("127.0.0.1", 12345, "input_state")

#osc receive
osc_receive = 0
finished = False

#mixer setting
pygame.mixer.init()

#1
osc_method("/state_receive", handlerfunction)
state = osc_receive
play_voice(filename1)


msg = oscbuildparse.OSCMessage("/event_state", None, [state])
osc_send(msg, "input_state")

#2
osc_method("/state_receive", handlerfunction)
state = osc_receive

play_voice(filename2)

msg = oscbuildparse.OSCMessage("/event_state", None, [state])
osc_send(msg, "input_state")

#3
osc_method("/state_receive", handlerfunction)
state = osc_receive

play_voice(filename3)

msg = oscbuildparse.OSCMessage("/event_state", None, [state])
osc_send(msg, "input_state")


#4
osc_method("/state_receive", handlerfunction)
state = osc_receive

play_voice(filename4)

msg = oscbuildparse.OSCMessage("/event_state", None, [state])
osc_send(msg, "input_state")

finished = True

while not finished:
    osc_process()

osc_terminate()
