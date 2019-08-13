#!/usr/bin/env python
import numpy
from scipy.ndimage import morphology as morp
from scipy import ndimage

def thresholding(img,threshold=0.9):
  if numpy.max(img) > 1 or numpy.min(img) < 0:
    print 'warning!!! image can be distorted becuase the range of image is not 0~1'
  
  img_ = numpy.copy(img)
  img_[img>=threshold] = 1
  img_[img<threshold] = 0
  return img_

def remain_digncomp(img):
  img_ = numpy.zeros(img.shape)
  for digpnt in range(img.shape[0]):
    img_[digpnt,digpnt] = 1

    # up direction
    movpnt = digpnt - 1
    while movpnt >= 0 and img[movpnt,digpnt] == 1:
	img_[movpnt,digpnt] = 1
	movpnt -= 1

    # left direction
    movpnt = digpnt - 1
    while movpnt >= 0 and img[digpnt,movpnt] == 1:
	img_[digpnt,movpnt] = 1
	movpnt -= 1

    # down direction
    movpnt = digpnt + 1
    while movpnt < img.shape[0] and img[movpnt,digpnt] == 1:
	img_[movpnt,digpnt] = 1
	movpnt += 1

    # right direction
    movpnt = digpnt + 1
    while movpnt < img.shape[0] and img[digpnt,movpnt] == 1:
	img_[digpnt,movpnt] = 1
	movpnt += 1

  return img_

def closing(img,sqaure_size):
  img_ = morp.binary_closing(img,structure=numpy.ones((sqaure_size,sqaure_size))).astype(int)
  return img_
    
def opening(img,sqaure_size):
  img_ = morp.binary_opening(img,structure=numpy.ones((sqaure_size,sqaure_size))).astype(int)
  return img_

def eliminate_comp(img,sqaure_size):
  n = sqaure_size
  label_im, nb_labels = ndimage.label(img)
  sizes = ndimage.sum(img, label_im, range(nb_labels + 1))
  mask_size = sizes < n*n
  remove_pixel = mask_size[label_im]
  label_im[remove_pixel] = 0
  img_ = numpy.copy(label_im)
  img_[img_>0] = 1

  return img_

def remain_sylrepcomp(img,repsize):
  uptrimat = numpy.triu(numpy.ones(img.shape))
  rm_dig_img = img * uptrimat
  label_im, nb_labels = ndimage.label(rm_dig_img)
  
  for lab in numpy.arange(1,nb_labels+1):
    findob = ndimage.find_objects(label_im==lab)
    if findob:
      slice_x, slice_y = ndimage.find_objects(label_im==lab)[0]
      comp_im = label_im[slice_x, slice_y]
      if comp_im.shape[0] < repsize or comp_im.shape[1] < repsize:
        label_im[slice_x,slice_y] = 0

  img_ = numpy.copy(label_im)
  img_[img_>1] = 1
  return img_

    
