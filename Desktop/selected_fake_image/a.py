import imghdr
import os

files = os.listdir('ready')

for file in files:
    out = imghdr.what('ready\\' + file)
    if out not in ['jpg', 'jpeg']:
        print(out, file)