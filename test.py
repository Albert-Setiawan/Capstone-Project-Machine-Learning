import cv2
import urllib
import numpy as np
from urllib.request import urlopen
from urllib.request import Request
import time
import json
import requests
import tensorflow as tf
kitab={"0":"Acne","1":'Eksim',"2":"Normal","3":"Rosacea"}
start_time=time.time()
if cv2.waitKey() & 0xff == 27: quit()
with urllib.request.urlopen(Request('http://answers.opencv.org/upfiles/logo_2.png', headers={'User-Agent': 'Mozilla/5.0'})) as resp:
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image,-1)
    np_image = tf.image.resize(image, (180, 180))/255
    np_image = np.expand_dims(np_image, axis=0)
    start_time=time.time()
    url="http://34.101.232.105:8081/v1/models/skut_testing:predict"
    data=json.dumps({"signature_name":"serving_default","instances":np_image.tolist()})
    headers={"content_type":"application/json"}
    response=requests.post(url,data=data,headers=headers)
    prediction=json.loads(response.text)['predictions']
    prediction=prediction[0]
    prediction=[round((x*100),2) for x in prediction]
    result={}
    for i in range(len(prediction)):
        result[kitab.get(str(i))]=str(prediction[i])+"%"
    with open("prediction.json", "w") as outfile:
        json.dump(result, outfile)