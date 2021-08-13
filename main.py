import os
import json

from flask import Flask, jsonify
from firebase_admin import credentials, firestore, initialize_app

app = Flask(__name__)

# Initialize Firestore DB
cred = credentials.Certificate('key.json')
default_app = initialize_app(cred)
db = firestore.client()
counter_ref = db.collection(u'counter').document(u'm9GEDCgdE2FPf6Cim9QG')

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
        return jsonify(doc.to_dict()), 200
    except Exception as e:
        return f"An Error Occured: {e}"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))