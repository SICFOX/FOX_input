import re
import snowboy.snowboydecoder
import os.path
import sys
import argparse
from osc4py3.as_eventloop import *
from osc4py3 import oscbuildparse
from mutagen.mp3 import MP3 as mp3
import pygame
import requests
from time import sleep

osc_udp_client("127.0.0.1", 12345, "input_state")
osc_udp_server("127.0.0.1", 12345, "state_receive")

#read .pmdl File
dir = os.path.dirname(os.path.abspath(__file__))

#You say "Hey, FOX".
HOTWORD_FILE = dir + "voice/FOX.pmdl"

#再生したいmp3ファイル
filename1 = 'voice/intro.mp3'
filename2 = 'voice/face_expression.mp3'
filename3 = 'voice/hand_sign.mp3'
filename4 = 'voice/wait.mp3'

#osc receive
osc_message = 0
finished = False

#osc setup
osc_startup()

#OSCでstateを送信する。
def make_osc(state):
    msg = osc_message_builder.OscMessageBuilder(address= "/event_state")
    msg.add_arg(state)
    msg = msg.build()

    return msg

#callback function
def handlerfunction(msg):
    osc_message = msg;

#Hey, FOXでの掛け声で呼び出されるイベント
def detected_callback():
    pygame.mixer.init()

    #1
    osc_method("/state_receive", handlerfunction)
    state = osc_message
    msg = oscbuildparse.OSCMessage("/event_state", None, [state])
    osc_send(msg, "input_state")
    osc_process()

    pygame.mixer.music.load(filename1)
    mp3_length = mp3(filename1).info.length
    pygame.mixer.music.play(1)
    sleep(mp3_length + 0.25)
    pygame.mixer.music.stop()
    
    #2
    osc_method("/state_receive", handlerfunction)
    state = osc_message
    msg = oscbuildparse.OSCMessage("/event_state", None, [state])
    osc_send(msg, "input_state")
    osc_process()

    pygame.mixer.music.load(filename2)
    mp3_length = mp3(filename2).info.length
    pygame.mixer.music.play(1)
    sleep(mp3_length + 0.25)
    pygame.mixer.music.stop()

    #3
    osc_method("/state_receive", handlerfunction)
    state = osc_message
    msg = oscbuildparse.OSCMessage("/event_state", None, [state])
    osc_send(msg, "input_state")
    osc_process()

    pygame.mixer.music.load(filename3)
    mp3_length = mp3(filename3).info.length
    pygame.mixer.music.play(1)
    sleep(mp3_length + 0.25)
    pygame.mixer.music.stop()

    #4
    osc_method("/state_receive", handlerfunction)
    state = osc_message
    msg = oscbuildparse.OSCMessage("/event_state", None, [state])
    osc_send(msg, "input_state")
    osc_process()

    pygame.mixer.music.load(filename4)
    mp3_length = mp3(filename4).info.length
    pygame.mixer.music.play(1)
    sleep(mp3_length + 0.25)
    pygame.mixer.music.stop()

state = 0
msg = oscbuildparse.OSCMessage("/event_state", None, [state])
osc_send(msg, "input_state")
osc_process()

detector = snowboydecoder.HotwordDetector(HOTWORD_FILE, sensitivity=0.5)
detector.start(detected_callback=detected_callback)

while not finished:
    osc_process()

osc_terminate()
