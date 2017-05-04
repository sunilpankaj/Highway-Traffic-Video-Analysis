# TRAFFIC-ANALYSIS-WITHOUT-MOTION-FEATURES

Previous Work and Problem:

Current traffic monitoring systems all rely on spatio-temporal features. These features are typically used to segment and track vehicles to compute traffic flow.  For it to work, they need high frame rate videos with stable environmental conditions.cameras often send to the server one frame every 2 or 3 second.The limited bandwidth makes it hard to have more than 2 frames per second.  So using this method they can analyse traffic on limited number of unregistered images.


Download UCSD traffic dataset datasets form here which contains 254 highway videos with different-different weather, place, time.

Classes are given for each videos:

First saparatevideos into 3 classes heavy, medium, light.
Now get 10 images per frame from videos for each catagory make 3 folder different folders of each class.
getimage.py = for getting images from videos.
