# set up the environment
import numpy as np

# %matplotlib inline # use this if you are using jupyter notebook
import matplotlib.pyplot as plt

# load the eeg data that Vic or Iran prepared using matlab for you
eeg_data = np.genfromtxt('calm', delimiter=',')

SR = 512.0

import scipy as sp
from scipy.io.wavfile import read # allows us to read in wave files

print 'the length of the eeg_data is:', len(eeg_data)

duration = len(eeg_data)/SR

print 'which in time duration is: ' , duration, ' seconds'

# generate a time vector
time = np.linspace(0,duration,len(eeg_data))

# let's see our raw data!!!!
plt.plot(time, eeg_data)
plt.show()
from scipy.io.wavfile import write # import to write out wave files

eeg_data=eeg_data/np.amax(eeg_data)

write('eegData.wav',512,eeg_data)

# Now we can do the fft 
eeg_data_fft = np.fft.fft(eeg_data)

# let's keep only the positive frequencies
eeg_data_fft_p = eeg_data_fft[0:len(eeg_data_fft)/2]

print 'This is a sample value in the fft: ', eeg_data_fft_p[438]

eeg_data_fft_p_abs = np.abs(eeg_data_fft_p)

eeg_data_fft_p_abs_db = 20*np.log10(eeg_data_fft_p_abs)

# let's generate a frequency axis
freq = np.linspace(0,SR/2,len(eeg_data_fft_p_abs_db))

# let's have a look at the fft of the data
plt.plot(freq,eeg_data_fft_p_abs_db)
plt.show()