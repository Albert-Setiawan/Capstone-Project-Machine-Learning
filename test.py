import PIL
import requests
import io
from PIL import Image

response=requests.get('https://cdn.discordapp.com/attachments/961628290953650176/984838589785460836/unknown.png')
image_bytes=io.BytesIO(response.content)
image=Image.open(image_bytes)
image.show()