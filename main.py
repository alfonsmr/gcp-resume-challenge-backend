import os
import json
import googlecloudprofiler
import googleclouddebugger

from flask import Flask, jsonify
from firebase_admin import credentials, firestore, initialize_app

app = Flask(__name__)

# Initialize Firestore DB
cred = credentials.Certificate('key.json')
default_app = initialize_app(cred)
db = firestore.client()
counter_ref = db.collection(u'counter').document(u'm9GEDCgdE2FPf6Cim9QG')

# Initialize Google CLoud Profiler

try:
    googlecloudprofiler.start(
        service='gcp-resume-challenge-counter',
        service_version='1.0.1',
        # verbose is the logging level. 0-error, 1-warning, 2-info,
        # 3-debug. It defaults to 0 (error) if not set.
        verbose=3,
        # project_id must be set if not running on GCP.
        # project_id='my-project-id',
    )
except (ValueError, NotImplementedError) as exc:
    print(exc)  # Handle errors here

try:
  googleclouddebugger.enable(
    breakpoint_enable_canary=False
  )

except ImportError:
  pass

@app.route('/', methods=['GET'])
def get_counter():
    """
        update() : Update document in Firestore collection with request body
        Ensure you pass a custom ID as part of json body in post request
        e.g. json={'id': '1', 'title': 'Write a blog post today'}
    """
    try:
        counter_ref.update({u'total': firestore.Increment(1)})
        doc = counter_ref.get()
        response = jsonify(doc.to_dict()), 200
        response.headers.add('Access-Control-Allow-Origin', 'https://gcp-resume-challenge.alfonsmr.com')
        return response
    except Exception as e:
        return f"An Error Occured: {e}"

# test 1
@app.route('/hello')
def hello():
  return "Hello World!\n"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))