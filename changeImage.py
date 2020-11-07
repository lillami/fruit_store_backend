#!/usr/bin/env python3

'''Final exam 1st part

upload the new images to the online store
images
descriptions
using: 2 different web endpoints'''

#transforming and converting images
import os, sys
from PIL import Image

path = '~/supplier-data/images'
content = os.listdir(path)

for infile in content:
    f, extension = os.path.splitext(infile)
    outfile = f + ".jpeg"
    if infile != outfile:
        try:
            with Image.open("~/images/", mode='r') as im:
                im.rotate(90).resize((600,400)).save("~/supplier-data/images", format = ".jpeg").convert("RGBA", "RGB")
        except OSError:
            print("cannot convert", infile)
