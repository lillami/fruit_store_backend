#! /usr/bin/env python3

'''
To add fruit images and their descriptions from the supplier on the fruit catalog web-server,
create a new Python script that will automatically POST the fruit images and
their respective description in JSON format.

To process the text files (001.txt, 003.txt ...) from the supplier-data/descriptions directory.
The script should turn the data into a JSON dictionary by adding all the required fields,
including the image associated with the fruit (image_name), and uploading it to
http://[linux-instance-external-IP]/fruits using the Python requests library.
'''


import os, sys
import requests
import json


# Path to the data
path = "supplier-data/descriptions/"

#iterate through the description and file names
folder = os.listdir(path)

for file in folder:
  if file.endswith("txt"):
      feedback = {}
      with open(path + file, 'r') as file_lines:
          #split the name of file + extension with splitext
        fruit_ID = os.path.splitext(file)[0]
        file_content = file_lines.read()
        file_content = file_content.split("\n")

            #grab the name and add .jpeg to it
        feedback = {
          "name": file_content[0],
          "weight": int(file_content[1].strip(" lbs")),
          "description": file_content[2],
          "image_name": fruit_ID + ".jpeg"}

          #post it
        response = requests.post("http://35.239.241.181/fruits/", json=feedback)
        response.raise_for_status()
        print(response.request.url)
        print(response.status_code)
