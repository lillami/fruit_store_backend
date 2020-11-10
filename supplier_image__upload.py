#!/usr/bin/env python3

'''
copy paste example_upload.py

takes the jpeg images from the ____supplier-data/images directory____ that you've processed previously
and uploads them to the ____web server fruit catalog____'''

import requests, os

url = "http://localhost/upload/"
path = '~/supplier-data/images'
pics = os.listdir(path)

for pic in pics:
    with open('~/supplier-data/images', 'rb') as opened:
        r = requests.post(url, files={'file': opened})
