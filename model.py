import os
import pandas
import h5py

import librosa.core as libcore
import numpy as np
from scipy.ndimage.interpolation import zoom

import utils

from keras.layers import Input,LSTM
from keras.layers.core import RepeatVector
from keras.models import Sequential
from keras.models import Model

%matplotlib inline
import matplotlib.pyplot as plt
from keras.callbacks import ModelCheckpoint


class Model(object):
    
    def __init__(self):
        self.done_training =False
        self.done_prediction =False
        self.INPUT_DIM = (N_FFT // 4) // 2
        self.SEQ_LEN = (SEQ_TIME * STFT_FPS + 1) // 2
        self.SAMPLING_RATE = 2048
        self.N_FFT = 256
        self.SEQ_TIME = 5
        self.CHUNK_SIZE = SEQ_TIME * SAMPLING_RATE
        self.HOP_LENGTH = N_FFT // 4
        self.STFT_FPS = SAMPLING_RATE // HOP_LENGTH
        self.position =None
        self.TS_SIZE = 2500
        self.load_data(CLEAN_DIR='Clean/')
        self.signals ={}
        self.powers ={}
        self.batch_size = 10
        self.training_set = self.train_partition()
        self.modelfn =self.model()
    
    
    def load_data():
        for f in tqdm(os.listdir(CLEAN_DIR)):
            samples, _ = libcore.load(CLEAN_DIR + f, sr=SAMPLING_RATE)
            power = np.mean(samples ** 2) * 0.5
            signals[f] = samples
            powers[f] = power
            
    def train_partition():
        training_set = np.array([sample_chunk(list(signals.values())[i],
                                              list(powers.values())[i]).T for i in range(len(os.listdir('Clean')))])
        return training_set

        
    def sample_chunk(samples, power, size=CHUNK_SIZE):
        if self.position is None:
            self.osition = int(np.random.uniform(high=len(samples) - size))    
        
        chunk = samples[position : position + size] / power  
    
    spectrum = np.log(np.abs(libcore.stft(chunk, n_fft=N_FFT)) + 1)[0 : N_FFT // 4] / 10.0        
    spectrum = zoom(spectrum, zoom=0.5)
    
    return spectrum    
        
        
    def model():
        # input layer
        inputs = Input(shape=(self.SEQ_LEN, self.INPUT_DIM))
        #encoder 
        enc = LSTM(100, activation ='relu')(inputs)
        # feature layer  with repeat vector
        features =RepeatVector(self.SEQ_LEN)(enc)
        #decoder layer
        dec = LSTM(self.INPUT_DIM, activation ='relu',return_sequences =True)(features)
        autoencoder =Model(inputs, dec)
        model_cb = ModelCheckpoint('output/lstm-{epoch:d}-{val_loss:.3f}.hdf', 
                                   monitor='val_loss', verbose=0, save_best_only=False,
                                    save_weights_only=False, mode='auto', period=10)
        if done_training:
            return
        history = autoencoder.fit(training_set, training_set, epochs=50, validation_split=0.1, callbacks=[model_cb])
        self.done_training =True
        summary =autoencoder.summary()
    
    return (autoencoder,summary,history) 
   
    def predict(model):
        
        if self.done_prediction:
            return
        model = self.modelfn
        
        batch_input = sample_chunk(samples, power, self.position=0, size=self.CHUNK_SIZE * 
                                   (self.batch_size + 1))

        stride = self.SEQ_LEN // 4 
        batch = np.array([batch_input[:, i * stride : i * stride + SEQ_LEN].T for i in range(batch_size * 4)])
        prediction = autoencoder.predict(batch)
        
        self.done_prediction =True
        
        return prediction
        
        
        
    
        
    