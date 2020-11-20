#!/usr/bin/env python3
'''
Using the reportlab Python library, define the method generate_report to build the PDF reports.
Create a PDF report named processed.pdf.
'''

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


def generate_method(filename, title, info):
  styles = getSampleStyleSheet()
  report = SimpleDocTemplate(filename)
  report_title = Paragraph(title, styles["h1"])
  report_info = Paragraph(info, styles["BodyText"])
  empty_line = Spacer(1,20)

  report.build([report_title, empty_line, report_info, empty_line])
