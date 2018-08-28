#python label_detection.py (APIキー) (画像ファイルのパス)
#api_key AIzaSyCYzlittDbDrELqOMGn77-LYLiuplMnvgA

from base64 import b64encode
from sys import argv
import json
import requests

ENDPOINT_URL = 'https://vision.googleapis.com/v1/images:annotate'

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

    # for idx, resp in enumerate(response.json()['responses']):
    #     print(json.dumps(resp, indent=2))
    a = response.json()['responses'][0]['faceAnnotations'][0]['joyLikelihood']
    b = response.json()['responses'][0]['faceAnnotations'][0]['sorrowLikelihood']
    c = response.json()['responses'][0]['faceAnnotations'][0]['angerLikelihood']
    d = response.json()['responses'][0]['faceAnnotations'][0]['surpriseLikelihood']
    print("joyLikelihood: "+ a)
    print("sorrowLikelihood: "+ b)
    print("angerLikelihood: "+ c)
    print("surpriseLikelihood: "+ d)
