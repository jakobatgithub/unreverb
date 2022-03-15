import numpy as np
import scipy.signal as ss
import soundfile as sf
import rir_generator as rir

# A script to generate the Impulse Response (IR) Functions of a rectangular room
# of a given size with given receiver and source positions and given Reverberation time T60.

# https://github.com/audiolabs/rir-generator
# pip install rir-generator
# pip install SoundFile

#signal, fs = sf.read("bark.wav", always_2d=True)

samplerate = 8000

reverberation_times = [0.4, 0.6, 0.8]
idx = 0
for reverberation_time in reverberation_times:
    IR_data = rir.generate(
    	c=340,                  # Sound velocity (m/s)
    	fs=samplerate,                  # Sample frequency (samples/s)
    	r=[                     # Receiver position(s) [x y z] (m)
    	    [4.5, 2.5, 1.5]
    	],
    	s=[0.5, 2.5, 1.5],          # Source position [x y z] (m)
    	L=[5, 5, 3],            # Room dimensions [x y z] (m)
    	reverberation_time=reverberation_time, # Reverberation time T60 (s)
    	nsample=samplerate,           # Number of output samples
	)
    print(IR_data.shape)              # (4096, 3)
    sf.write('random_IRs/IRF_'+str(idx)+'.wav', IR_data, samplerate)
    idx = idx +1	

#print(signal.shape)         # (11462, 2)

# Convolve 2-channel signal with 3 impulse responses
#signal = ss.convolve(h[:, None, :], signal[:, :, None])

#print(signal.shape)         # (15557, 2, 3)
