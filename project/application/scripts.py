import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt
import pickle
import cv2
import os, sys

IMG_SIZE = 500
TEST_DATADIR = "D:\\SUBJECTS FOLDER\\Minor\\Datasets\\Healthy_and_Patient_Test_Dir\\Test"
def openFile():
    with open('C:\\Minor\\Minor_django\\project\\external_files\\model_svm.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

def prepare(img_name):
    path = os.path.join(TEST_DATADIR, img_name)
    image_array = cv2.imread(path, 3)
    #print(image_array.shape)
    latest_array = cv2.resize(image_array, (IMG_SIZE,IMG_SIZE))
    #plt.imshow(latest_array)
    #plt.show()
    #print(latest_array.shape)
    latest_array = latest_array.reshape(1,IMG_SIZE*IMG_SIZE*3)
    latest_array = latest_array/255.0 
    return latest_array