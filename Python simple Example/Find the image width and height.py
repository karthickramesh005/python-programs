# Find the image width and height :

import PIL
from PIL import Image

img = PIL.Image.open("C:\Users\karthick R\Pictures\tony\wallpaperflare.com_wallpaper.jpg")
width,height = img.size

print(width,"*",height)
