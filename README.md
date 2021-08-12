# gcp-resume-challenge-backend
gcp-resume-challenge-frontend 

BACKEND

https://cloud.google.com/community/tutorials/building-flask-api-with-cloud-firestore-and-deploying-to-cloud-run
https://cloud.google.com/run/docs/quickstarts/build-and-deploy/python

import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("path/to/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

