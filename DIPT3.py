#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np
import matplotlib.pyplot as plt


# In[3]:


image = cv2.imread('JEEVI.png')

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# In[4]:


hist_original = cv2.calcHist([gray_image], [0], None, [256], [0, 256])


# In[5]:


equalized_image = cv2.equalizeHist(gray_image)

hist_equalized = cv2.calcHist([equalized_image], [0], None, [256], [0, 256])


# In[6]:


plt.figure(figsize=(10, 7))


# In[7]:


plt.subplot(2, 2, 1)
plt.imshow(gray_image, cmap='gray')
plt.title('Original Grayscale Image')
plt.axis('off');


# In[8]:


plt.subplot(2, 2, 2)
plt.imshow(equalized_image, cmap='gray')
plt.title('Equalized Image')
plt.axis('off');


# In[9]:


plt.subplot(2, 2, 3)
plt.plot(hist_original, color='black')
plt.title('Original Histogram')
plt.xlim([0, 256]);


# In[10]:


plt.subplot(2, 2, 4)
plt.plot(hist_equalized, color='black')
plt.title('Equalized Histogram')
plt.xlim([0, 256]);


# In[11]:


plt.tight_layout()
plt.show()


# In[ ]:




