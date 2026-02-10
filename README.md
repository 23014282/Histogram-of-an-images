# Histogram-of-an-images
## Aim
To obtain a histogram for finding the frequency of pixels in an Image with pixel values ranging from 0 to 255. Also write the code using OpenCV to perform histogram equalization.

## Software Required:
Anaconda - Python 3.7

## Algorithm:
### Step1:
Read the gray and color image using imread()

### Step2:
Print the image using imshow().



### Step3:
Use calcHist() function to mark the image in graph frequency for gray and color image.

### step4:
Use calcHist() function to mark the image in graph frequency for gray and color image.

### Step5:
The Histogram of gray scale image and color image is shown.


## Program:
# Developed By: JEEVITH
# Register Number: 212223240059
```python
import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('a.jpeg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
hist_original = cv2.calcHist([gray_image], [0], None, [256], [0, 256])

equalized_image = cv2.equalizeHist(gray_image)
hist_equalized = cv2.calcHist([equalized_image], [0], None, [256], [0, 256])
plt.figure(figsize=(10, 7))

plt.subplot(2, 2, 1)
plt.imshow(gray_image, cmap='gray')
plt.title('Original Grayscale Image')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.imshow(equalized_image, cmap='gray')
plt.title('Equalized Image')
plt.axis('off')

plt.subplot(2, 2, 3)
plt.plot(hist_original, color='black')
plt.title('Original Histogram')
plt.xlim([0, 256])

plt.subplot(2, 2, 4)
plt.plot(hist_equalized, color='black')
plt.title('Equalized Histogram')
plt.xlim([0, 256])

plt.tight_layout()
plt.show()
```
  
## Output:
### Input Grayscale Image and Color Image

<img width="315" height="262" alt="image" src="https://github.com/user-attachments/assets/8f736777-b363-456d-a9ba-e162da4be1c2" />

<img width="260" height="249" alt="image" src="https://github.com/user-attachments/assets/de4f1ad9-d6ee-4f72-aa3f-51d306b02e56" />




### Histogram of Grayscale Image and any channel of Color Image


<img width="465" height="282" alt="image" src="https://github.com/user-attachments/assets/ef9743bd-0f8f-4a63-a1fe-699edc0a7358" />




### Histogram Equalization of Grayscale Image.

<img width="472" height="273" alt="image" src="https://github.com/user-attachments/assets/9dfb12d0-512c-4c9c-94b1-178fc7e06a62" />





## Result: 
Thus the histogram for finding the frequency of pixels in an image with pixel values ranging from 0 to 255 is obtained. Also,histogram equalization is done for the gray scale image using OpenCV.
