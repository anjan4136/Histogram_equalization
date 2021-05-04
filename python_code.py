from matplotlib import pyplot as plt         #importing pyplot library from matplotlib, one use of this is it is used here for plotting the images
import numpy as np                           # It is used for numerical calculations as matrix calculations , data structures 
import cv2                                   #opencv this library has various image processing functions 
from google.colab.patches import cv2_imshow  #For us to able to see the image we have imported this.

src = cv2.imread("hawkes.jpg",0)             #for reading image from the system #o, for gray scale channel
print(src)                                   #printing image in terms of intensity levels
src.shape                                    #pixels in image size(x,y)

cv2_imshow(src)                              #To see the image before equalization
plt.hist(src.ravel(),256,[0,256])            #function/method for seeing histogram of an image 
plt.show()                                   #To see the histagram plot
dst = cv2.equalizeHist(src)                  #Method/Fuction in opencv used to equlaize the values of intensities in
                                             #histogram over the entire range of gray scale 0-256
cv2_imshow(dst)                              #To see the image after applying histogram equalization
plt.hist(dst.ravel(),256,[0,256])            #function/method for seeing histogram of an image 
plt.show()                                   #To see the histagram plot
