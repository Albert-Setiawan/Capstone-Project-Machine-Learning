import skimage
import numpy as np

image_filename = "https://upload.wikimedia.org/wikipedia/commons/f/f0/Acne_vulgaris_on_a_very_oily_skin.jpg"
image_numpy = skimage.io.imread( image_filename )
image_numpy=np.asarray(image_numpy).astype(np.float32)/255
print(image_numpy)