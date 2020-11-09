#!/usr/bin/env python3

'''
Generating pdf-s.

The text description processed from the text files as the paragraph argument, the report title as the title argument,
and the file path of the PDF to be generated as the attachment argument
'''

import os
import datetime
import reports


def generate_pdf(path):
  pdf = ""
  files = os.listdir(path)

  for file in files:
    if file.endswith(".txt"):
      with open(path + file, 'r') as f:
        inline = f.readlines()
        name = inline[0].strip()
        weight = inline[1].strip()
        pdf += "name:" + name + "<br>" + "weight:" + weight + "<br><br>"

  return pdf


if __name__ == "__main__":
    path = '/supplier-data/descriptions/'
    #process the data
    paragraph = generate_pdf(path)#text description processed from the text files
    title = "Process Update on the {}".format(date.today())
    reports.generate_report('/tmp/processed.pdf', title, paragraph)
