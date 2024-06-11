from flask import Flask, request, redirect, url_for, render_template
from google.cloud import storage
import os

app = Flask(__name__)

# Configure this environment variable with your GCS bucket name
os.environ["GOOGLE_CLOUD_PROJECT"] = "osticket-testing-425914"
BUCKET_NAME = 'bkt-sales-data-osticket-testing-425914'

def upload_to_gcs(file, bucket_name, destination_blob_name):
    """Uploads a file to Google Cloud Storage."""
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_file(file)
    return blob.public_url

@app.route('/')
def index():
    # Check if 'url' parameter exists in the query string
    upload_status = request.args.get('status')
    return render_template('index.html', upload_status=upload_status)

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return redirect(url_for('index', status='failure'))
    file = request.files['file']
    if file.filename == '':
        return redirect(url_for('index', status='failure'))
    if file:
        public_url = upload_to_gcs(file, BUCKET_NAME, file.filename)
        return redirect(url_for('index', status='success'))

if __name__ == '__main__':
    app.run(debug=True)
