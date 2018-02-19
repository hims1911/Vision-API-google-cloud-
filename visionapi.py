#!/usr/bin/env python
"""
Uses the Google Cloud Vision API,
for the annalysis of image
--important note--
as we have the
"""
#importing all the neccesarry files
import argparse
import base64
import csv
import httplib2
import datetime
import json
import os
from googleapiclient.discovery import build
from oauth2client.client import GoogleCredentials
import logging
logging.basicConfig(filename='debug.log',level=logging.DEBUG)

#for processing image
def process_images(image_input):
    image_exts = ['.bmp', '.gif', '.jpg', '.jpeg', '.png']
    if image_input[-1] == "/":
        dir_name = image_input

        for file_name in os.listdir(dir_name):
            ext = os.path.splitext(file_name)
        
            if file_name not in ignore_files and ext[1].lower() in image_exts and not os.path.isdir(fn):
                print(file_name)
                main(dir_name + file_name)
    else:
        print(image_input)
        main(image_input)


def main(photo_file):
    """Run a request on a single image"""

    API_DISCOVERY_FILE = 'https://vision.googleapis.com/$discovery/rest?version=v1'
    http = httplib2.Http()

    credentials = GoogleCredentials.get_application_default().create_scoped(
            ['https://www.googleapis.com/auth/cloud-platform'])
    credentials.authorize(http)

    service = build('vision', 'v1', http, discoveryServiceUrl=API_DISCOVERY_FILE)

    with open(photo_file, 'rb') as image:
        image_content = base64.b64encode(image.read())
        service_request = service.images().annotate(
                body={
                    'requests': [{
                        'image': {
                            'content': image_content
                        },
                        'features': [{
                            'type': 'LABEL_DETECTION',
                            'maxResults': 20,
                        },
                            {
                            'type': 'TEXT_DETECTION',
                            'maxResults': 20,
                            }]
                    }]
                })
    response = service_request.execute()

    # Prepare parsing of responses into relevant fields
    query = photo_file
    all_labels = ''
    all_text = ''

    try:
        labels = response['responses'][0]['labelAnnotations']
        for label in labels:
            # label = response['responses'][0]['labelAnnotations'][0]['description']
            label_val = label['description']
            score = str(label['score'])
            print('Found label: "%s" with score %s' % (label_val, score))
            all_labels += label_val.encode('utf-8') + ' @ ' + score + ', '
    except KeyError:
        print("N/A labels found")

    print('\n')

    try:
        texts = response['responses'][0]['textAnnotations']
        for text in texts:
            # text = response['responses'][0]['textAnnotations'][0]['description']
            text_val = text['description']
            print('Found text: "%s"' % text_val)
            all_text += text_val.encode('utf-8') + ', '
    except KeyError:
        print("N/A text found")

    print('\nIMAGE PROCESSING DONE\n')
    return 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('image_input', help='The folder containing images or the image you\'d like to query')
    args = parser.parse_args()
    process_images(args.image_input)