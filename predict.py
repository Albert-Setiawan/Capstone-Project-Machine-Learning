from matplotlib import image
import requests
import json
import numpy as np
import cv2
import tensorflow as tf
import time
import sys
kitab={"0":"Acne","1":'Eksim',"2":"Normal","3":"Rosacea"}

np_image = cv2.imread('D:\Bangkit2022/testing2.jfif')
np_image = np.array(np_image).astype('float32')/255
np_image = tf.image.resize(np_image, (180, 180))
np_image = np.expand_dims(np_image, axis=0)
start_time=time.time()
url=sys.argv[1]
data=json.dumps({"signature_name":"serving_default","instances":np_image.tolist()})
headers={"content_type":"application/json"}
response=requests.post(url,data=datapwd,headers=headers)
prediction=json.loads(response.text)['predictions']
value=max(prediction[0])
label=prediction[0].index(value)
print(value,label,kitab.get(str(label)))
