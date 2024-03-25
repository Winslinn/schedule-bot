from flask import Flask
from PIL import Image

app = Flask(__name__)

@app.route('/schedule', methods=['GET'])
def handle():
    return 'test'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)