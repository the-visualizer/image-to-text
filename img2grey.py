#img2grey.py
import numpy as np
from scipy import misc
import matplotlib.pyplot as plt

M = misc.imread('/home/visualizer/Desktop/input4.png')
grey = np.zeros(M.shape)

for rownum in range(len(M)):
	for colnum in range(len(M[0])):
		grey[rownum][colnum] = np.average(M[rownum][colnum])

misc.imsave('/home/visualizer/Desktop/Output4.png',grey)

#f, axarr = plt.subplots(1,2) # This 
#axarr[0,0].imshow(M)         # doesn't
#axarr[0,1].imshow(grey)      # work!

fig = plt.figure()
a=fig.add_subplot(1,2,1)
imgplot = plt.imshow(M)
a.set_title('Before')
a=fig.add_subplot(1,2,2)
imgplot = plt.imshow(grey)
a.set_title('After')
plt.show()

#The grayscale image is saved on the desktop.
#However, this image appears pixelated when displayed using imshow().