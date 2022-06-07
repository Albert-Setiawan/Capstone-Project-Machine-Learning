
#import modules
import numpy as np
import urllib.request
import cv2
from urllib.request import Request
import sys
  
# read the image url
url = sys.argv[1]

with urllib.request.urlopen(Request(url, headers={'User-Agent': 'Mozilla/5.0'})) as resp:
    
    # read image as an numpy array
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
      
    # use imdecode function
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    print(image.shape)
  
    # display image
    cv2.imshow("result.jpg", image)
    cv2.waitKey()