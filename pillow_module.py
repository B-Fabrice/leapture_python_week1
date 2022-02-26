from PIL import Image
import os, sys

img = Image.open('kjsdnkjs.png')
# print(img.format)
# print(img.size)
# print(img.height)
# print(img.width)
# print(img.info)
# img.show()

#Convert img to JPEG

jpgimg = img.convert('RGB')
# jpgimg.save('jpg_converted.jpg')
# jpgimg.show()


#create thumbnails from JPEG

# conimg = img.convert('RGB')
# conimg.thumbnail((70, 70))
# conimg.save('thumbnail.jpg')
# conimg.show()

#resize img
# resizedImg = img.resize((150, 150))
# resizedImg.show()