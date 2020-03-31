import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt
import cv2
import os, sys
import pickle
from PIL import Image
LABELS = ['Healthy', 'Patient']
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXTERNAL_DIR = os.path.join(BASE_DIR, 'external_files')
TEST_DATADIR = os.path.join(BASE_DIR, 'media')
def openFile_svm():
    with open(os.path.join(EXTERNAL_DIR, 'model_parkinson_svm_spiral.pkl'), 'rb') as file:
        model = pickle.load(file)
        file.close()
    return model

def openFile_naive_bayes():
    with open(os.path.join(EXTERNAL_DIR, 'model_parkinson_bayes_spiral.pkl'), 'rb') as file:
        model = pickle.load(file)
        file.close()
    return model

def prepare(img_name):
    image_fullpath = sys.argv[1]
    image_name = sys.argv[2]

    image = Image.open(str(image_fullpath))
    image_save_path = image_fullpath.replace(image_name, 'temp.jpg')
    image.save(image_save_path)

    print('\media\temp.jpg')

    IMG_SIZE = 400
    path = os.path.join(TEST_DATADIR, img_name)
    """path,"""
    #DIR = str(image_save_path)
    image_array = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    #image_array = cv2.imread(image_name, cv2.IMREAD_GRAYSCALE)
    #print(image_array.shape)
    latest_array = cv2.resize(image_array, (IMG_SIZE,IMG_SIZE))
    #plt.imshow(latest_array)
    #plt.show()
    #print(latest_array.shape)
    latest_array = latest_array.reshape(1,IMG_SIZE*IMG_SIZE)
    latest_array = latest_array/255.0
    return latest_array


def main_function_svm():
    model = openFile_svm()
    prediction = LABELS[model.predict(prepare('temp.jpg'))[0]]
    print('',prediction)
    
def main_function_naive_bayes():
    model = openFile_naive_bayes()
    prediction = LABELS[model.predict(prepare('temp.jpg'))[0]]
    print('',prediction)
    
#main_function_naive_bayes()
main_function_svm()
