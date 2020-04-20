# TRAFFIC-ANALYSIS-WITHOUT-MOTION-FEATURES

Previous Work and Problem:

Current traffic monitoring systems all rely on spatio-temporal features. These features are typically used to segment and track vehicles to compute traffic flow.  For it to work, they need high frame rate videos with stable environmental conditions.cameras often send to the server one frame every 2 or 3 second.The limited bandwidth makes it hard to have more than 2 frames per second.  So using this method they can analyse traffic on limited number of unregistered images.

Download UCSD traffic dataset: contains 254 highway videos with different-different weather, place, time.

Classes are given for each videos.

Method: this method is working with 2fps 

1. extract local image features of all training images (e.g. HOG or SIFT).

2. generate a codebook from these features (e.g. k-means, GMM ) and encode local image features into visual descriptors.

3. train a classifie.

First separate videos into 3 classes heavy, medium, light.

Now get 10 images per frame from videos for each catagory make 3 folder different folders of each class.

getimage.py = for getting images from videos.

Unsupervised Task: Here 2fps will be used. get sift features and using k-mean (k = number of feature) generates codebook 

Now using this codebook or dictionary find the bag of visual word for each image and assign label and save into csv file.

features.py: will create dictionary and make bag of visual word and finaly making cav file of heavy , medium, light.csv files 
which we will use for prediction. 

feutures_k5.py = will generates 5 features from each image

feutures_k10.py = will generates 10 features from each image

feutures_k15.py = will generates 15 features from each image

feutures_k30.py = will generates 30 features from each image

feutures_k100.py = will generates 100 features from each image

feutures_folder: You can find all csv file corresponding to each file.

Now combine all csv file (light, medium, heavy) for each k (features) and make prediction using svm, Adaboost, randomforest, extratree clasifie.

We are getting the best accuracy (95.38%) using ExtraTreesClassifier for 100 features or value of k = 100.

classk_5.ipynb for k = 5 features

classk_10.ipynb for k = 10 features

classk_30.ipynb for k = 30 features

classk_100.ipynb for k = 100 features

plot.py for plotting accuracy of each model for different-different k for comparing model.

Result_folder:  all output images.

Result: confusion matrix for extratreeclasifier for k 100

![screenshot from 2017-05-01 00 51 38](https://cloud.githubusercontent.com/assets/14961825/25705587/71dbbf38-30fb-11e7-94f5-2840e440ff87.png)

Comparing Model: 

1. k = 100

![screenshot from 2017-05-01 00 43 18 2](https://cloud.githubusercontent.com/assets/14961825/25705818/3f966432-30fc-11e7-9831-3c385fd469ed.png)

2. k =30 

![screenshot from 2017-05-01 00 43 06 2](https://cloud.githubusercontent.com/assets/14961825/25705881/73570ace-30fc-11e7-87a5-c13f3fa1b6f0.png)

3. k = 10

![screenshot from 2017-05-01 00 42 28 2](https://cloud.githubusercontent.com/assets/14961825/25705944/9cd8bc76-30fc-11e7-8744-9feec5c48f35.png)

4. k = 5

![screenshot from 2017-05-01 00 42 09 2](https://cloud.githubusercontent.com/assets/14961825/25705982/c1e6a94c-30fc-11e7-9402-8d99ef1aec77.png)


References:  http://ieeexplore.ieee.org/document/7351412/
