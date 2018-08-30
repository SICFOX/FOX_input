import re
from snowboy import snowboydecoder
import os.path
import sys
import argparse
from python_osc.pythonosc import osc_message_builder
from python_osc.pythonosc import udp_client
from mutagen.mp3 import MP3 as mp3
import pygame
import requests
from time import sleep

#OSC setup
port_num = 12345
parser = argparse.ArgumentParser()
parser.add_argument("--ip", default="127.0.0.1", help="The ip of th OSC Server")
parser.add_argument("--port", type=int, default=port_num, help="The port the OSC server is listening on")
args = parser.parse_args()
client = udp_client.UDPClient(args.ip, args.port)

#read .pmdl File
dir = os.path.dirname(os.path.abspath(__file__))
#You say "Hey, FOX".
HOTWORD_FILE = dir + "/voice/FOX.pmdl"

filename1 = '/voice/intro.mp3' #再生したいmp3ファイル
filename2 = '/voice/face_expression.mp3'
filename3 = '/voice/hand_sign.mp3'
filename4 = '/voice/wait.mp3'

#OSCでstateを送信する。
def make_osc(state):
    msg = osc_message_builder.OscMessageBuilder(address= "/event_state")
    msg.add_arg(state)
    msg = msg.build()

    return msg

#Hey, FOXでの掛け声で呼び出されるイベント
def detected_callback():
    pygame.mixer.init()

    state = 1
    osc_msg = make_osc(state)
    client.send(osc_msg)

    pygame.mixer.music.load(filename1)
    mp3_length = mp3(filename1).info.length
    pygame.mixer.music.play(1)
    sleep(mp3_length + 0.25)
    pygame.mixer.music.stop()

    state = 2
    osc_msg = make_osc(state)
    client.send(osc_msg)

    pygame.mixer.music.load(filename2)
    mp3_length = mp3(filename2).info.length
    pygame.mixer.music.play(1)
    sleep(mp3_length + 0.25)
    pygame.mixer.music.stop()

    state = 3
    osc_msg = make_osc(state)
    client.send(osc_msg)

    pygame.mixer.music.load(filename3)
    mp3_length = mp3(filename3).info.length
    pygame.mixer.music.play(1)
    sleep(mp3_length + 0.25)
    pygame.mixer.music.stop()

    state = 4
    osc_msg = make_osc(state)
    client.send(osc_msg)

    pygame.mixer.music.load(filename4)
    mp3_length = mp3(filename4).info.length
    pygame.mixer.music.play(1)
    sleep(mp3_length + 0.25)
    pygame.mixer.music.stop()

state = 0
osc_msg = make_osc(state)
client.send(osc_msg)

detector = snowboydecoder.HotwordDetector(HOTWORD_FILE, sensitivity=0.5)
detector.start(detected_callback=detected_callback)
