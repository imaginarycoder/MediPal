import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle
import cv2
import os, sys

def openFile():
    with open('C:\\Minor\\Minor_django\\project\\pickle_files\\model_svm.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

if __name__ == '__main__':
    openFile()
