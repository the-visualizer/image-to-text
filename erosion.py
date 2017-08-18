import os, sys, scipy
from scipy import ndimage
import matplotlib.pyplot as plt 
import numpy as np 
from PIL import Image

inFile = ''
outFile = ''

if len(sys.argv) !=3:
    print ('Input format error!')
else:
    inFile = sys.argv[1]
    outFile = sys.argv[2]

#im = ndimage.imread(inFile) 
#im = ndimage.binary_erosion(im).astype(np.float32)
#scipy.misc.imsave(outFile, im)

#im2 = Image.open(inFile)
#im2 = ndimage.binary_dilation(im2)

im = scipy.misc.imread(inFile, flatten=True).astype(np.uint8)
im2 = ndimage.grey_erosion(im, size=(100,10))

scipy.misc.imsave(outFile, im2)
