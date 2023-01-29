import os
from flask import Flask, render_template, send_from_directory
import random

app = Flask(__name__, static_folder='static', static_url_path='/static')

# port = int(os.environ.get("PORT", 5000))
# app.run(host='0.0.0.0', port=port)

@app.route('/index')
def index():
    images = os.listdir('static/images')
    random_image = random.choice(images)
    return render_template('index.html', image=random_image)

@app.route('/static/images/<path:filename>')
def image(filename):
    return send_from_directory(app.static_folder + '/images', filename)

if __name__ == "__main__":
    app.run()

@app.route("/refresh_image")
def refresh_image():
    images = os.listdir('static/images')
    random_image = random.choice(images)
    return random_image