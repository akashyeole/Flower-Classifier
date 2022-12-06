import numpy as np
from utils import CATEGORIES
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
import cv2
import tensorflow as tf
import os, shutil

app = Flask(__name__)
model = tf.keras.models.load_model('model.h5')
# UPLOAD_FOLDER = 'uploads'
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods = ['POST'])
def predict():
    for filename in os.listdir('static/uploads'):
        file_path = os.path.join('static/uploads', filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
    file = request.files['sample']
    filename = secure_filename(file.filename)
    file.save(os.path.join('static\\uploads', filename))
    # os.remove(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    img_path = os.path.join('static\\uploads', filename)
    image = cv2.imread(img_path)
    image = cv2.resize(image, (224, 224))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB).astype(np.float32)
    image = image / 255.0
    img_batch = np.expand_dims(image, axis=0)
    model = tf.keras.models.load_model('model.h5')
    prediction = model.predict(img_batch)


    return render_template('afterpred.html', imgurl = 'static/uploads/'+filename, result = CATEGORIES[np.argmax(prediction[0])].upper(), accuracy = max(prediction[0]) * 100)


if __name__ == "main":
    app.run(debug = True)