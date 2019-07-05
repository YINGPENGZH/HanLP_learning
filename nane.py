import tensorflow as tf
from skimage import io,transform
import matplotlib.pyplot as plt
img=io.imread("G://BaiduXJTU/train_data/train/1319954370,1647454103.jpg")
io.imshow(img)
image_sigle = io.imread("G://BaiduXJTU/train_data/train/2718383308,2466713207.jpg");
I = transform.resize(image_sigle,(200,200))
io.imsave('G://BaiduXJTU/train_data/train_resize/dog.jpg',I)
filePath="G://BaiduXJTU/train_data/data_train_image.txt"
plt.imshow(I);
plt.show()

def readFile_print(filePath):
    fopen = open(filePath, 'r') # r 代表read
    for eachLine in fopen:
        print(eachLine.split()[0])
    fopen.close()

readFile_print(filePath)