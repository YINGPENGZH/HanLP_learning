'''
HelloWorld example using TensorFlow library.
Author: Aymeric Damien
Project: https://github.com/aymericdamien/TensorFlow-Examples/
'''


from __future__ import print_function
import os
import skimage.io as io
from skimage import io,transform

# f = open("label_name.txt","r",encoding='UTF-8')
# lines = f.readlines();
# for line in lines:
#     print (line)
filePath="G://BaiduXJTU/train_data/data_train_image.txt"
filepath='G://BaiduXJTU/train_data/train'


# def readFile(filePath):
#     fopen = open(filePath, 'r') # r 代表read
#     for eachLine in fopen:
#         # print(eachLine.split())
#         temp=eachLine.split()[0:2]
#         name=''.join(temp[0])
#         label=''.join(temp[1])
#         f = open('G://BaiduXJTU/train_data/my.txt','a')
#         f.write('G://BaiduXJTU/train_data/train/'+name+'.jpg'+' '+label+'\n')
#     fopen.close()

# eachFile(filepath);
mytxt='G://BaiduXJTU/train_data/my.txt'
# def img_resize(filePath):
#     imgs= open(filePath,'r');
#     for img in imgs:
#         temp = img.split();
#         image_sigle = io.imread(temp[0]);
#         I = transform.resize(image_sigle,(300,300));
#         save_name=temp[0].replace('G://BaiduXJTU/train_data/train/','');
#         io.imsave('G://BaiduXJTU/train_data/train_resize/'+save_name,I);
# img_resize(mytxt)


fopen = open(filePath, 'r') # r 代表read
for eachLine in fopen:
    print(eachLine.split())
    temp=eachLine.split()[0:2]
    name=''.join(temp[0])
    label=''.join(temp[1])
    f = open('G://BaiduXJTU/train_data/resize_index.txt','a')
    f.write('G://BaiduXJTU/train_data/train_resize/'+name+'.jpg'+' '+label+'\n')
fopen.close()