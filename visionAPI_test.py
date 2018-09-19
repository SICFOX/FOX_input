#!/usr/bin/env python
# -*- coding: utf-8 -*-

#python visionAPI.py (画像ファイルのパス)
#api_key AIzaSyCYzlittDbDrELqOMGn77-LYLiuplMnvgA

from base64 import b64encode
from sys import argv
import json
import requests
import serial

ENDPOINT_URL = 'https://vision.googleapis.com/v1/images:annotate'

#Serial Port
#ser = serial.Serial('/dev/cu.wchusbserial1420', 9600)

if __name__ == '__main__':
    image_filenames = argv[1:]

    img_requests = []
    for imgname in image_filenames:
        with open(imgname, 'rb') as f:
            ctxt = b64encode(f.read()).decode()
            img_requests.append({
                    'image': {'content': ctxt},
                    'features': [{
                        'type': 'FACE_DETECTION',
                        'maxResults': 5
                    }]
            })

    response = requests.post(ENDPOINT_URL,
                             data=json.dumps({"requests": img_requests}).encode(),
                             params={'key': 'AIzaSyCYzlittDbDrELqOMGn77-LYLiuplMnvgA'},
                             headers={'Content-Type': 'application/json'})

#IPAdress Error
    if not image_filenames:
        print("Please specify API key and image file properly. $ python visionAPI.py image.jpg")
    else:
        if response.status_code != 200 or response.json().get('error'):
            print(response.text)

    if not response.json()['responses'][0]:
        #ser.write(0)
        print(0)

    if response.json()['responses'][0]:
        a = response.json()['responses'][0]['faceAnnotations'][0]['joyLikelihood']
        b = response.json()['responses'][0]['faceAnnotations'][0]['sorrowLikelihood']
        c = response.json()['responses'][0]['faceAnnotations'][0]['angerLikelihood']
        d = response.json()['responses'][0]['faceAnnotations'][0]['surpriseLikelihood']

        emotion = {1:a, 2:b, 3:c, 0:d}

        for key, value in emotion.items():
            if value == 'VERY_LIKELY':
                #ser.write(key)
                print(key)

        if a == 'VERY_UNLIKELY' or b == 'VERY_UNLIKELY' or c == 'VERY_UNLIKELY' or d == 'VERY_UNLIKELY':
            #ser.write(key)
            print(0)




