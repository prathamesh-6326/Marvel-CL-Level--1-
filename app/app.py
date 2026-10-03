import os, boto3
from flask import Flask, request

app = Flask(__name__)
s3 = boto3.client("s3")  # reads AWS_* env vars automatically
BUCKET = os.environ["S3_BUCKET"]

FORM = """<h2>Upload to S3</h2>
<form method=post action=/upload enctype=multipart/form-data>
<input type=file name=file><button>Upload</button></form>"""

@app.get("/")
def index():
    return FORM

@app.post("/upload")
def upload():
    f = request.files["file"]
    s3.upload_fileobj(f, BUCKET, f.filename)
    return f"Uploaded {f.filename} to s3://{BUCKET}/{f.filename}\n"

app.run(host="0.0.0.0", port=5000)
