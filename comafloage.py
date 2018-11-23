
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
import argparse
import utils
import cv2
from imutils import paths
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
ap.add_argument("-c", "--clusters", required = True, type = int,
	help = "# of clusters")
args = vars(ap.parse_args())
 
# load the image and convert it from BGR to RGB so that
# we can dispaly it with matplotlib
image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
 
# show our image
plt.figure()
plt.axis("off")
plt.imshow(image)

# reshape the image to be a list of pixels
image = image.reshape((image.shape[0] * image.shape[1], 3))
img = np.zeros((512,512,3), np.uint8)
# cluster the pixel intensities
clt = KMeans(n_clusters = args["clusters"])
clt.fit(image)

# build a histogram of clusters and then create a figure
# representing the number of pixels labeled to each color
hist = utils.centroid_histogram(clt)

bar,colorOb = utils.plot_colors(hist, clt.cluster_centers_)



i = 0
perceHist=hist
while(i<len(hist)):
    perceHist[i]=hist[i]*100
    #print("Histogram :",perceHist[i])
    i=i+1
#b=cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)
 
# show our color bart
plt.figure()
plt.axis("off")
plt.imshow(bar)
#plt.imshow(b)

plt.show()







