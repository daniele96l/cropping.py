import pandas as pd
import cv2
import numpy as np
from data import sorted_list

#df = pd.read_csv('excel1.csv')
folder = "/Users/danieleligato/Desktop/Thesis/point_projection/Cam1/"
 
w_r = 2048
h_r = 2448


for i in range(len(sorted_list)):
    
    x,y,w,h = [sorted_list[i][0], sorted_list[i][1], sorted_list[i][2], sorted_list[i][3]]
    x = float(x)
    y = float(y)
    w = float(w)
    h = float(h)
    x_start = int((x-w/2)*w_r)
    x_end = int((x+w/2)*w_r)
    y_start = int((y-h/2)*h_r)
    y_end = int((y+h/2)*h_r)
    image = cv2.imread(folder+'202107280658_Rectified_'+str(sorted_list[i][5])+'_Cam1.jpg')
    
    #if(y_end-y_start > 20): size filter
    crop = image[y_start:y_end,x_start:x_end]
    cv2.imwrite('crops/crop_'+str(sorted_list[i][5])+'_' +str(i) +'.png'.format(i), crop)
    
