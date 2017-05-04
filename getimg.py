import numpy as np
import cv2
import glob

count = 0
for vid in glob.glob("trafficdb/light/*.avi"):
	vidcap = cv2.VideoCapture(vid)
	success,image = vidcap.read()
	success = True
	while success:
	  success,image = vidcap.read()
	  print 'Read a new frame: ', success
	  cv2.imwrite("trafficdb/light_images/light%d.jpg" % count, image)     # save frame as JPEG file
	  count += 1
	print count

