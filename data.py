import os
from tqdm import tqdm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from python_speech_features import mfcc, logfbank
import librosa



def find_fft(signal, rate):
    n = len(signal)
    freq = np.fft.rfftfreq(n ,d =1/rate)
    Y = np.abs(np.fft.rfft(signal)/n)
    return (Y, freq)





#plot signals

def plot_signals(signals):
    fig, axes =plt.subplots(nrows =2, ncols=5,sharex=False,sharey=True,figsize=(20,5))
    fig.suptitle("Time series",size =16)
    i =0
    for x in range(2):
        for y in range(5):
            axes[x,y].set_title(lists(signals).keys()[i]) 
            axes[x,y].plot(lists(signals).values()[i])
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
            i += 1
    
    
def plot_fbank(fbank):
    fig, axes =plt.subplots(nrows =2, ncols=5,sharex=False,sharey=True,figsize=(20,5))
    fig.suptitle("Filter bank coefficients",size =16)
    i =0
    for x in range(2):
        for y in range(5):
            axes[x,y].set_title(lists(fbank).keys()[i]) 
            axes[x,y].plot(lists(fbank).values()[i])
            i += 1

            
def plot_mfcc(mfccs):
    fig, axes =plt.subplots(nrows =2, ncols=5,sharex=False,sharey=True,figsize=(20,5))
    fig.suptitle("Mfccs",size =16)
    i =0
    for x in range(2):
        for y in range(5):
            axes[x,y].set_title(lists(mfccs).keys()[i]) 
            axes[x,y].plot(lists(mfccs).values()[i])
            i += 1
                
            

fft ={}
fbank ={}
signals ={}
mfccs ={}

for f in os.listdir('AllAudioWav'):
    signal,rate =librosa.load('AllAudioWav/'+f,sr=2048)
    signals[f] = signal
    fft[f] =find_fft(signal,rate)
    bank =logfbank(signal[:rate], rate, nfilt  =26, nfft=51).T
    fbank[f] =bank
    mel =mfcc(signal[:rate], rate, numcep =13, nfilt =26, nfft =51).T
    mfccs[f] = mel
    

plot_signals(signals)
plt.show()

plot_fft(fft)
plt.show()

plot_fbank(fbank)
plt.show()

plot_mfcc(mfccs)
plt.show()
    
            
            
            
            
            
            
            
            
