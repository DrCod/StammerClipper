#!/usr/bin/env python
import numpy
import pickle
import matplotlib.pyplot as plt

def savepckdata(out_file,data):
  print "save data -> ", out_file
  pck = open(out_file,'wb')
  pickle.dump(data,pck)
  pck.close()

def loadpckdat(in_file):
  print "load data -> ", in_file
  pck = open(in_file,'rb')
  data = pickle.load(pck)
  pck.close()
  return data

def saveprorepimg(out_file,img_pro,img_rep):
  # format(tuple) : [img_pro_size array(pro_data) array(rep_data)] 
  # img_pro_size = output[0]
  # array(pro_data) = output[1]
  # array(rep_data) = output[2]
  print "save prolongation and repetition image ->", out_file
  pro_size = img_pro.shape[0]
  rep_size = img_rep.shape[0]
  if not pro_size == rep_size:
    print "error!! do not equalize the size of image between prolongation and repetition"
    raise

  out_data = []
  inx = numpy.arange(pro_size*pro_size)
  inx = numpy.reshape(inx,(pro_size,pro_size))
  data_pro = inx[img_pro>0]
  data_rep = inx[img_rep>0]

  out_data.append(pro_size)
  out_data.append(data_pro)
  out_data.append(data_rep)

  pck = open(out_file,'wb')
  pickle.dump(out_data,pck)
  pck.close()

def loadprorepimg(in_file,pause=0):
  # format(tuple) : [img_pro_size array(pro_data) array(rep_data)] 
  # img_pro_size = output[0]
  # array(pro_data) = output[1]
  # array(rep_data) = output[2]
  if not pause :
    print "load prolongation and reptition image ->", in_file
  pck = open(in_file,'rb')
  load_data = pickle.load(pck)
  img_size = int(load_data[0])
  pro_data = load_data[1]
  rep_data = load_data[2]
  if not (img_size or pro_data or rep_data):
    print "error!!!! the load data wrong : ", in_file
    raise

  pro_img = numpy.zeros((img_size*img_size,1))
  rep_img = numpy.zeros((img_size*img_size,1))
  pro_img[pro_data] = 1
  rep_img[rep_data] = 1
  pck.close()
  return numpy.reshape(pro_img,(img_size,img_size)), numpy.reshape(rep_img,(img_size,img_size)) 

def plotprorepimg(in_file):
  pro_img, rep_img = loadprorepimg(in_file)
  plt.figure(1)
  plt.subplot(121)
  plt.title('Prolongation')
  plt.imshow(pro_img,cmap='gray')

  plt.subplot(122)
  plt.title('Repetition')
  plt.imshow(rep_img,cmap='gray')
  plt.show() 





