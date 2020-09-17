#!/usr/bin/env python
# coding: utf-8

import cv2
from xgboost import XGBClassifier, Booster
import xgboost as xgb
import numpy as np
import matplotlib.pyplot as plt


xgb_model = xgb.XGBClassifier()
xgb_model.load_model('xgb_final_1m_extended.bin')


aerial_sampled_img = cv2.imread("1_m_aerial_final.tif")
aerial_sampled_img = cv2.cvtColor(aerial_sampled_img, cv2.COLOR_BGR2RGB)

print('Image loaded')

def flatten_image(image):
    return image.reshape((image.shape[0] * image.shape[1], *image.shape[2:]))   


def predict_on_image(model, image):
    flat_image = flatten_image(image)
    y_pred = model.predict(flat_image)
    prediction_colours = np.zeros((y_pred.shape[0], 3))
    colour_mapping = {
        0: (11, 102, 35),
        1: (134, 136, 138),
        2: (198, 162, 66),
        3: (10, 17, 114), 
        4: (75, 58, 38)
    }
    for i in range(y_pred.shape[0]):
        prediction = y_pred[i]
        prediction_colour = np.array(colour_mapping[prediction])
        prediction_colours[i] = prediction_colour
    
    return prediction_colours.reshape(image.shape), y_pred

print('Starting predictions')

aerial_predictions, y_pred = predict_on_image(xgb_model, aerial_sampled_img)

print('Done with predictions, saving image')

np.save('total_aerial_pred_colours_1m.npy', aerial_predictions)
np.save('total_aerial_predictions_1m.npy', y_pred)

# plt.imsave('aerial_predictions_1m.png', aerial_predictions, format='png')

print('Done!')
