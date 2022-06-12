from matplotlib.pyplot import axis
import requests
import json
import numpy as np
import cv2
import tensorflow as tf
import time

image=cv2.imread('testing3.jfif')
image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
image=cv2.resize(image,(180,180))/255
image=np.expand_dims(image,axis=0)

url='http://34.101.232.105:8081/v1/models/skut_testing:predict'
data=json.dumps({'signature_name':"serving_default","instances":image.tolist()})
headers={'content-type':'application/json'}
response=requests.post(url,data=data,headers=headers)
prediction=json.loads(response.text)['predictions']
print(prediction)