import requests
import json
import numpy as np
import cv2
import tensorflow as tf
import time
import sys
from PIL import Image
import io
kitab={"0":"Acne","1":'Eksim',"2":"Normal","3":"Rosacea"}
start_time=time.time()
url = sys.argv[1]
response=requests.get(url)
image_bytes=io.BytesIO(response.content)
image=Image.open(image_bytes)
np_image=cv2.cvtColor(np.array(image),cv2.COLOR_BGR2RGB)
np_image=cv2.resize(np_image,(180,180))/255
np_image=np.expand_dims(np_image,axis=0)
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
