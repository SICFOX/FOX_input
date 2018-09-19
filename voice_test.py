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
import socket

host = "127.0.0.1" #Processingで立ち上げたサーバのIPアドレス
port = 10001       #Processingで設定したポート番号

filename1 = 'voice/intro.mp3'
filename2 = 'voice/face_expression.mp3'
filename3 = 'voice/hand_sign.mp3'
filename4 = 'voice/wait.mp3'

def play_voice(filename):
    pygame.mixer.music.load(filename)
    mp3_length = mp3(filename).info.length
    pygame.mixer.music.play(1)
    sleep(mp3_length + 0.25)
    pygame.mixer.music.stop()


if __name__ == '__main__':
    socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #オブジェクトの作成
    socket_client.connect((host, port))                               #サーバに接続
    pygame.mixer.init()

    socket_client.send('1'.encode('utf-8')) #データを送信 Python3
    response = socket_client.recv(4096).decode('utf-8')
    print(response)
    play_voice(filename1)

    socket_client.send('2'.encode('utf-8')) #データを送信 Python3
    response = socket_client.recv(4096).decode('utf-8')
    print(response)
    play_voice(filename2)

    socket_client.send('3'.encode('utf-8')) #データを送信 Python3
    response = socket_client.recv(4096).decode('utf-8')
    print(response)
    play_voice(filename3)

    socket_client.send('4'.encode('utf-8')) #データを送信 Python3
    response = socket_client.recv(4096).decode('utf-8')
    print(response)
    play_voice(filename4)
