# module for working with image data
from PIL import Image
from matplotlib import image as mpimg
from matplotlib import pyplot as plt
import numpy as np

# filePath for our test picture
testAbbyFilePath = r"C:\Users\sebid\Downloads\IMG_0129.jpg"

# load our test image
abby = Image.open(testAbbyFilePath)

# some details about the test pic
print(abby.format)
print(abby.mode)
print(abby.size)

# show abby
abby.show()

# greyscale abby
greyscaleAbby = abby.convert(mode="L")

greyscaleAbby.show()

# turn abby into numbers
abbyArray = asarray(abby)




