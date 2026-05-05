from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return '''<html><head><title>Devi DevOps Project</title></head>
    <body style="font-family:Arial;text-align:center;padding:50px;background:#0a0e1a;color:white;">
    <h1>Hello from Devi Jayavelu</h1>
    <h2>DevOps Portfolio Project</h2>
    <p>Running on Docker + Kubernetes + GCP</p>
    <p style="color:#00d4aa">Infrastructure provisioned with Terraform</p>
    </body></html>'''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
