#!/usr/bin/env python3

'''
takes the jpeg images from the __supplier-data/images directory__ processed previously
and uploads them to the __web server fruit catalog__
'''

import requests, os

url = "http://localhost/upload/"
path = 'supplier-data/images/'
pics = os.listdir(path)

for pic in pics:
    with open('path+pic', 'rb') as opened:
        r = requests.post(url, files={'file': opened})
