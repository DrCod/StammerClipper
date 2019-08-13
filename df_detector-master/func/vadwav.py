#!/usr/bin/env python
# webrtcvad 
#   Copyright (C) 2016 John Wiseman
#   author : John Wiseman jjwiseman@gmail.com
#   license : MIT
# vadwav
#   modified by byjang 2016.12.06
#   author : Byeong-Yong Jang darkbulls44@gmail.com

import scipy
from scipy.io import wavfile
import webrtcvad
import collections
import matplotlib.pyplot as plt
import numpy

def frame_generator(frame_duration_ms, audio, sample_rate):
    n = int(sample_rate * (frame_duration_ms / 1000.0) * 2)
    offset = 0
    while offset + n < len(audio):
        yield audio[offset:offset + n]
        offset += n

def vad_collector(sample_rate, frame_duration_ms,
                  padding_duration_ms, vad, frames):
    num_padding_frames = int(padding_duration_ms / frame_duration_ms)
    ring_buffer = collections.deque(maxlen=num_padding_frames) # processing for last N(maxlen) data
    triggered = False
    voiced_frames = []
    vad_index = []
    for frame in frames:
        #sys.stdout.write('1' if vad.is_speech(frame, sample_rate) else '0')
        if not triggered:
	    vad_index.extend(scipy.zeros(len(frame)))
            ring_buffer.append(frame)
            num_voiced = len([f for f in ring_buffer
                              if vad.is_speech(f, sample_rate)])
            if num_voiced > 0.9 * ring_buffer.maxlen:
                #sys.stdout.write('+')
		vad_index[len(vad_index)-num_padding_frames*len(frame):len(vad_index)] = scipy.ones(num_padding_frames*len(frame))
                triggered = True		
                voiced_frames.extend(ring_buffer)
                ring_buffer.clear()
        else:
	    vad_index.extend(scipy.ones(len(frame)))
            voiced_frames.append(frame)
            ring_buffer.append(frame)	    
            num_unvoiced = len([f for f in ring_buffer
                                if not vad.is_speech(f, sample_rate)])
            if num_unvoiced > 0.9 * ring_buffer.maxlen:
                #sys.stdout.write('-')
		vad_index[len(vad_index)-num_padding_frames*len(frame):len(vad_index)] = scipy.zeros(num_padding_frames*len(frame))
                triggered = False
		yield (list(voiced_frames), vad_index)
                ring_buffer.clear()
                voiced_frames = []
    if voiced_frames:
        yield (list(voiced_frames), vad_index)
    

def run(wav_file,vad_aggressive=0,frame_duration=10,padding_duration=50):

	# parameters
	# wav_file : path of wav file
	# vad_aggressive=0 # 0~3 (least ~ most agrressive)
	# frame_duration = 10 # (ms)
	# sample_rate = 16000 # sample_rate must be 8k, 16k, 32k
			      # because a frame must be either 10, 20, or 30 ms in duration
	# padding_duration = 50 # (ms) vad padding duration
	
	# read wave data
	print 'read wav file - ', wav_file
	(sf, wav_data) = wavfile.read(wav_file)
	if sf != 16000 and sf != 8000 and sf != 32000:
	  print 'error!!! sample rate of wav is not 8k, 16k, or 32kHz'
	  print 'the sample rate of this file is %d' % (sf)
	  raise	

	print 'processing VAD ...'
	# VAD
	vad = webrtcvad.Vad()
	vad.set_mode(vad_aggressive)
	frames = frame_generator(frame_duration, wav_data, sf)
	frames = list(frames)
	segments = vad_collector(sf,frame_duration,padding_duration, vad, frames)

	vad_data = []
	print 'chunking wav ...',
	for i, (segment, vad_index) in enumerate(segments):
	  print '%d' % (i),
	  for frame in segment:
	    vad_data.extend(frame)
	print 'done'

	# convert to range : -32768 ~ 32767 -> -1 ~ 1
	vad_data = numpy.array(vad_data)/float(2**15-1)

	ori_data = wav_data
	return (vad_data, vad_index, ori_data, sf)

def plotvad(vad_data,vad_index,wav_data,fignum):
	# VAD index padding with length of wav data
	if len(vad_index) != len(wav_data) :
	  pad_size = len(wav_data) - len(vad_index)
	  vad_index.extend(scipy.zeros(pad_size))

	# normalizing
	no_data = wav_data/float(2**15-1) # range -1 ~ 1
	vad_index = numpy.array(vad_index)*max(no_data)

	# plot wav and VAD index
	plt.figure(fignum)
	plt.title('Signal wave and vad index...')
	plt.plot(no_data)
	plt.plot(vad_index,color="red")
	#plt.show()


