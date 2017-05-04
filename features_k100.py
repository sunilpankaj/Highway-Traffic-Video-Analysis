import numpy as np
import cv2
import cv
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import csv
sift = cv2.SIFT()

dictionarySize = 100

BOW = cv2.BOWKMeansTrainer(dictionarySize)
#using only lights images
for i in range(0,869):
    image = cv2.imread('light_images\light%d.jpg' % (i*10))
    if ( image != None):
        gray = cv2.cvtColor(image, cv2.CV_LOAD_IMAGE_GRAYSCALE)
        kp, dsc= sift.detectAndCompute(gray, None)
        #print dsc
        BOW.add(dsc)
#using only heavy images
for i in range(0,230):
    image = cv2.imread('heavy_images\heavy%d.jpg' % (i*10))
    if ( image != None):
        gray = cv2.cvtColor(image, cv2.CV_LOAD_IMAGE_GRAYSCALE)
        kp, dsc= sift.detectAndCompute(gray, None)
        #print dsc
        BOW.add(dsc)
 #using only medium images       
for i in range(0,224):
    image = cv2.imread('medium_images\medium%d.jpg' % i*10)
    if ( image != None):
        gray = cv2.cvtColor(image, cv2.CV_LOAD_IMAGE_GRAYSCALE)
        kp, dsc= sift.detectAndCompute(gray, None)
        #print dsc
        BOW.add(dsc)
        
#dictionary created
dictionary = BOW.cluster()
#print dictionary

with open('feature_dictonary.txt', 'wb') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_NONNUMERIC)
    for row in dictionary :
        wr.writerow(row)

l = len(dsc)


FLANN_INDEX_KDTREE = 0
index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
search_params = dict(checks=50)   # or pass empty dictionary
flann = cv2.FlannBasedMatcher(index_params,search_params)
sift2 = cv2.DescriptorExtractor_create("SIFT")
bowDiction = cv2.BOWImgDescriptorExtractor(sift2, cv2.BFMatcher(cv2.NORM_L2))


bowDiction.setVocabulary(dictionary)


print "bow dictionary", np.shape(dictionary)


# making featurs file of only light images
with open('hist_light.txt', 'wb') as myfile:

    for i in range(0,869):
        image = cv2.imread('light_images\light%d.jpg' % (i*10))
        if ( image != None):
            gray = cv2.cvtColor(image, cv2.CV_LOAD_IMAGE_GRAYSCALE)
            kp, dsc= sift.detectAndCompute(gray, None)
            hist = bowDiction.compute(gray,kp)
            wr = csv.writer(myfile, quoting=csv.QUOTE_NONNUMERIC)
            for row in hist:
                wr.writerow(row)
        print hist

# making featurs file of only heavy images

with open('hist_heavy.txt', 'wb') as myfile:

    for i in range(0,230):
        image = cv2.imread('heavy_images\heavy%d.jpg' % (i*10))
        if ( image != None):
            gray = cv2.cvtColor(image, cv2.CV_LOAD_IMAGE_GRAYSCALE)
            kp, dsc= sift.detectAndCompute(gray, None)
            hist = bowDiction.compute(gray,kp)
            wr = csv.writer(myfile, quoting=csv.QUOTE_NONNUMERIC)
            for row in hist:
                wr.writerow(row)
        print hist

# making featurs file of only medium images

with open('hist_medium.txt', 'wb') as myfile:

    for i in range(0,224):
        image = cv2.imread('medium_images\medium%d.jpg' % i*10)
        if ( image != None):
            gray = cv2.cvtColor(image, cv2.CV_LOAD_IMAGE_GRAYSCALE)
            kp, dsc= sift.detectAndCompute(gray, None)
            hist = bowDiction.compute(gray,kp)
            wr = csv.writer(myfile, quoting=csv.QUOTE_NONNUMERIC)
            for row in hist:
                wr.writerow(row)
        print hist
