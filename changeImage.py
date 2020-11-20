#!/usr/bin/env python3

#transforming and converting images
import os, sys
from PIL import Image

path = 'supplier-data/images/'
content = os.listdir(path)

for infile in content:
    f = os.path.splitext(infile)[0]
    outfile = path + f + ".jpeg"
        try:
            with Image.open(path+infile).rotate(90).resize((600,400)).convert("RGB").save(outfile, format = "JPEG")
        except OSError:
            print("cannot convert", infile)
