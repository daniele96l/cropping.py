from data import sorted_list
import cv2

df = sorted_list
image = cv2.imread('202107280658_Rectified_601_Cam1.jpg')

x_c = 0.4384765625
y_c = 0.4384765625
w = 0.005859375
h = 0.00449346425011754

w_r = 2400
h_r = 2000
xstart = (x_c - w/2)*h_r
xstop = (x_c + w/2)*h_r
ystart = (y_c - h/2)*w_r
ystop = (y_c + h/2)*w_r

crop = image[ystart:ystop, xstart:xstop]
print(crop)
cv2.imwrite("crop_{0}.png".format(0), crop)