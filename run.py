#! /usr/bin/env python3

'''
To add fruit images and their descriptions from the supplier on the fruit catalog web-server,
create a new Python script that will automatically POST the fruit images and
their respective description in JSON format.

to process the text files (001.txt, 003.txt ...) from the supplier-data/descriptions directory.
The script should turn the data into a JSON dictionary by adding all the required fields,
including the image associated with the fruit (image_name), and uploading it to
http://[linux-instance-external-IP]/fruits using the Python requests library.
'''


import os, sys
import requests
import json


# Path to the data
path = "/supplier-data/descriptions/"

keys = ["name", "weight", "description", "image_name"]

folder = os.listdir(path)
for file in folder:
    keycount = 0
    fb = {}
    with open(path + file) as fl:
        for line in fl:
            value = line.strip()
            if type(weight) == int:
              pass
            elif:
              return int(''.join(i for i in weight.split('lbs')[0] if i.isdigit()))
        
            #iterate through the description file names
            
            #split the name without extension with splitext
            
            #grab the name and add .jpeg to it
        
            fb[keys[keycount]] = value
            keycount += 1
    print(fb)
    response = requests.post("http://<IP Address>/fruits/",
    json=fb)
print(response.request.body)
print(response.status_code)


'''
The data model in the Django application fruit has the following fields: name, weight, description and image_name.
The weight field is defined as an integer field. So when you process the weight information of the fruit from the .txt file,
you need to convert it into an integer. For example if the weight is "500 lbs",

#you need to drop "lbs" and
#convert "500" to an integer.

The image_name field will allow the system to find the image associated with the fruit. Don't forget to add all fields,
including the image_name! The final JSON object should be similar to:

{"name": "Watermelon", "weight": 500, "description": "Watermelon is good for relieving heat, eliminating annoyance
and quenching thirst. It contains a lot of water, which is good for relieving the symptoms of acute fever immediately.
The sugar and salt contained in watermelon can diuretic and eliminate kidney inflammation. Watermelon also contains
substances that can lower blood pressure.", "image_name": "010.jpeg"}
'''
