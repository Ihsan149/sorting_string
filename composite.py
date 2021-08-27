# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 16:15:35 2021

@author: Khan
"""
import cv2
import numpy
import glob
from os import listdir
import itertools
import os
import itertools
import re

def natural_sort_key(s, _nsre=re.compile('([0-9]+)')):
    return [
        int(text)
        if text.isdigit() else text.lower()
        for text in _nsre.split(s)]

def read_img():
    path ="G:/Catheter_Dataset/tracking_data/videos/"
    img_list =[]
    for root, dirs, files in sorted(os.walk(path)):
        for file in files:
            if(file.endswith(".png")):
                # print(os.path.join(root,file))
                img = cv2.imread(os.path.join(root,file))
                img_list.append(os.path.join(root,file))
                # cv2.imshow('img',img)
                # mask, mask_path = read_mask()
                # cv2.waitKey(0)
    return img_list

def read_mask():
    path ="G:/Catheter_Dataset/tracking_data/manually labeled data/train/masks types/1/"
    mask_list = []
    for root, dirs, files in sorted(os.walk(path)):
        for file in files:
            if(file.endswith(".png")):
                # print(os.path.join(root,file))
                mask = cv2.imread(os.path.join(root,file))
                mask_list.append(os.path.join(root,file))
                # cv2.imshow('mask',mask)
                # cv2.waitKey(0)
    return mask_list
            
img_list = read_img()
mask_list = read_mask()
sorted_images = sorted(img_list, key=natural_sort_key)
sorted_mask = sorted(mask_list, key=natural_sort_key)
# mask_list = sorted(mask_list)
# print(mask_list)

for i,m in itertools.zip_longest(sorted_images,itertools.cycle(sorted_mask)):
    print(i)
    pateint_no = i.split('/')[4]
    print(pateint_no)
    image_name =os.path.basename(i)
    print(image_name)
    img = cv2.imread(i,0)
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.resize (img,(256,256), interpolation = cv2.INTER_AREA)
    cv2.imshow('img',img)
    img = img.astype(float)
    mask_ori = cv2.imread(m,0)
    mask = cv2.bitwise_not(mask_ori)
    cv2.imshow('mask',mask)
    
    # mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
    mask = cv2.resize (mask,(256,256), interpolation = cv2.INTER_AREA)
    # .astype(float)/255
    mask = mask.astype(float)/255
    
    foreground = cv2.multiply(mask, img/255)
    cv2.imshow('img_for',foreground)
    cv2.waitKey(0)
    if i is None:
        break
