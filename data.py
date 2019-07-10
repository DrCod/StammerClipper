import os
from tqdm import tqdm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from python_speech_features import mfcc, logfbank
import librosa


#plot signals

def plot_signals(signals):
    fig, axes =plt.subplots(nrows =2, ncols=5,sharex=False,sharey=True,figsize=(20,5))
    fig.suptitle("Time series",size =16)
    i =0
    for x in range(2):
        for y in range(5):
            axes[x,y].set_title(lists(signals).keys()[i]) 
            axes[x,y].plot(lists(signals).values()[i])
            axes[x,y].get_xaxis().setVisible(False)
            axes[x,y].get_yaxis().setVisible(False)
            i += 1
    
# plot fourier transformed signals    
def plot_fft(fft):
    fig, axes =plt.subplots(nrows =2, ncols=5,sharex=False,sharey=True,figsize=(20,5))
    fig.suptitle("FFT",size =16)
    i =0
    for x in range(2):
        for y in range(5):
            axes[x,y].set_title(lists(fft).keys()[i]) 
            axes[x,y].plot(lists(fft).values()[i])
            axes[x,y].get_xaxis().setVisible(False)
            axes[x,y].get_yaxis().setVisible(False)
            i += 1
    
    
def plot_fbank(fbank):
    fig, axes =plt.subplots(nrows =2, ncols=5,sharex=False,sharey=True,figsize=(20,5))
    fig.suptitle("Filter bank coefficients",size =16)
    i =0
    for x in range(2):
        for y in range(5):
            axes[x,y].set_title(lists(fbank).keys()[i]) 
            axes[x,y].plot(lists(fbank).values()[i])
            axes[x,y].get_xaxis().setVisible(False)
            axes[x,y].get_yaxis().setVisible(False)
            i += 1
            
            
         

            
            
            
            
            
            
            
            
