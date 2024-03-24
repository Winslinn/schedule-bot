from flask import Flask
from PIL import Image

app = Flask(__name__)

@app.route('/employees', methods=['GET'])
def handle():
    return 'Test'