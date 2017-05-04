# TRAFFIC-ANALYSIS-WITHOUT-MOTION-FEATURES

Previous Work and Problem:

Current traffic monitoring systems all rely on spatio-temporal features. These features are typically used to segment and track vehicles to compute traffic flow.  For it to work, they need high frame rate videos with stable environmental conditions.cameras often send to the server one frame every 2 or 3 second.The limited bandwidth makes it hard to have more than 2 frames per second.  So using this method they can analyse traffic on limited number of unregistered images.


Download UCSD traffic dataset datasets form here which contains 254 highway videos with different-different weather, place, time.

Classes are given for each videos.

Method: this method is working with 2fps 

1. extract local image features of all training images (e.g. HOG or SIFT).

2. generate a codebook from these features (e.g. k-means, GMM ) and encode local image features into visual descriptors.

3. train a classifie.

First saparatevideos into 3 classes heavy, medium, light.

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

Now combine all csv file (light, medium, heavy) for each k (features) and make prediction using svm, decision_tree, randomforest, extratree clasifie.

classk_5.ipynb for k = 5 features

classk_10.ipynb for k = 10 features

classk_30.ipynb for k = 30 features

classk_100.ipynb for k = 100 features




