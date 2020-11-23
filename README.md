# fruit_store_backend
for my final exam

1. changeImage.py:transforming and converting images uploaded by suppliers

2. supplier_image_upload.py: takes the jpeg images converted before and uploads them to the web server

3. run.py: making sure that the descriptions find the matching pictures, then posting them in json format.

4. reports.py: will create pdf reports that will be sent regularly later on.

5. report_email.py: contains main() for reports.py and sends the email out

6. emails.py: for generating the emails with the pdf report attachments

7. I also made a health_check.py that is monitoring the system every 60 seconds and sends errors for given conditions as CPU, disk space and memory usage or if localhost cannot be resolved to 127.0.0.1. Unfortunately the time ran out I couldn't test it.
