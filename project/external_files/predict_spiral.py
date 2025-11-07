import numpy as np
import cv2
import os, sys
import tensorflow as tf
from PIL import Image

LABELS = ['Healthy', 'Unhealthy']
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXTERNAL_DIR = os.path.join(BASE_DIR, 'external_files')
TEST_DATADIR = os.path.join(BASE_DIR, 'media')

np.set_printoptions(suppress=True)

def model_load():
    model = tf.keras.models.load_model(os.path.join(EXTERNAL_DIR, 'keras_model_spiral.h5'), compile=False)
    return model

def prepare(image_name):

    image_fullpath = sys.argv[1]
    image_name = sys.argv[2]

    image = Image.open(str(image_fullpath))

    # To check if the image has an alpha channel present in PNG images (RGBA mode) or 'P' mode (palette-based)
    if image.mode in ('RGBA', 'P'):
        background = Image.new("RGB", image.size, (255, 255, 255))
        background.paste(image, mask = image.split()[3])
        image = background.convert('RGB')
    
    image_save_path = image_fullpath.replace(image_name, 'temp.jpg')
    image.save(image_save_path)

    test_image_path = os.path.join(TEST_DATADIR, image_name)
    image = cv2.imread(test_image_path)

    if image is None:
        print("Error: Image not loaded. Check the file path and name.")
    else:
        image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)
        image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)
        image = (image / 127.5) - 1

    return image

def predict():
    model = model_load()
    prediction = model.predict(prepare('temp.jpg'))
    index = np.argmax(prediction)

    class_name = LABELS[index]
    confidence_score = prediction[0][index]
    
    print("Result:", class_name, " and ", "Confidence:", str(np.round(confidence_score * 100))[:-2], "%")

predict()