from flask import Flask
from PIL import Image

app = Flask(__name__)

@app.route('/schedule', methods=['GET'])
def handle():
    return 'test'