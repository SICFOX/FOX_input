import re
import os.path
import sys
import argparse
from python_osc.pythonosc import osc_message_builder
from python_osc.pythonosc import udp_client
from pythonosc import dispatcher
from pythonosc import osc_server
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

#OSC setup
port_num = 12345
parser = argparse.ArgumentParser()
parser.add_argument("--ip", default="2127.0.0.1", help="The ip of th OSC Server")
parser.add_argument("--port", type=int, default=port_num, help="The port the OSC server is listening on")
args = parser.parse_args()
client = udp_client.UDPClient(args.ip, args.port)

def make_osc(state):
    msg = osc_message_builder.OscMessageBuilder(address= "/petiteco/direct2")
    msg.add_arg(state)
    msg = msg.build()
    
    return msg

#mixer setting
pygame.mixer.init()

#1

input_str3 = query
osc_msg3 = make_osc3(input_str3)
client.send(osc_msg3)



pygame.mixer.music.load(filename1)
mp3_length = mp3(filename1).info.length
pygame.mixer.music.play(1)
sleep(mp3_length + 0.25)
pygame.mixer.music.stop()

#2
pygame.mixer.music.load(filename2)
mp3_length = mp3(filename2).info.length
pygame.mixer.music.play(1)
sleep(mp3_length + 0.25)
pygame.mixer.music.stop()

#3
pygame.mixer.music.load(filename3)
mp3_length = mp3(filename3).info.length
pygame.mixer.music.play(1)
sleep(mp3_length + 0.25)
pygame.mixer.music.stop()

#4
pygame.mixer.music.load(filename4)
mp3_length = mp3(filename4).info.length
pygame.mixer.music.play(1)
sleep(mp3_length + 0.25)
pygame.mixer.music.stop()
