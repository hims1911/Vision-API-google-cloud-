# Vision-API-google-cloud-
Image Annalysis using Vision-API of Google Cloud Platform

### VISION-API:-
API written in Python in order to annalyse the image using Vision-api,Following command is used 
in order to run the python file
```
$ python visionapi.py [image or path to image]
```

### Setting Up:-
1)You'll need Google Developer account in order create the API key and to take care of the authentication details.
dont forget to set up your credentials for the CLI to work
```
 $export GOOGLE_APPLICATION_CREDENTIALS=<path to service key.json file>
```
2)As we used the Python Script to call the API we have to install the packages,using "pip  install" commands for
google-api-python-client",oauth2client.
```
$pip install apiclient
$pip install oauth2client
$pip install httplib2
```
3)Run the Script using above command that is
```
$python visionapi.py [image or path to image]
```

