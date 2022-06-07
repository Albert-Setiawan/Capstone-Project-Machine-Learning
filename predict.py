from matplotlib import image
import requests
import json
import numpy as np
import cv2
import tensorflow as tf
import time
import skimage
#import sys
kitab={"0":"Acne","1":'Eksim',"2":"Normal","3":"Rosacea"}
image_filename = "https://cdn11.bigcommerce.com/s-ydriczk/images/stencil/1280x1280/products/86669/93774/Justin-Bieber-Card-Party-Face-Mask-available-now-at-starstills__28645.1573577871.jpg"
np_image = skimage.io.imread( image_filename )
np_image=np.asarray(np_image).astype(np.float32)/255
np_image = tf.image.resize(np_image, (180, 180))
np_image = np.expand_dims(np_image, axis=0)
start_time=time.time()
url="http://localhost:8601/v1/models/skut_testing:predict"
data=json.dumps({"signature_name":"serving_default","instances":np_image.tolist()})
headers={"content_type":"application/json"}
response=requests.post(url,data=data,headers=headers)
prediction=json.loads(response.text)['predictions']
value=max(prediction[0])
label=prediction[0].index(value)
print(value,label,kitab.get(str(label)))
