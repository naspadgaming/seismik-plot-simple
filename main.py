import obspy
import obspy.core
import obspy.core.stream
import pqdm
import matplotlib.pyplot as plt

data = obspy.read("L8_24_0-46_-7_SP1_3.dat") #ini data seismiknya/aku pakai .dat
print(data)

print(data.__str__(extended=True))
tr=data[0]
tr.plot()
#sebenarnya buat ngeplot  cukup sampai disini aja

import numpy as np
trace_data = data[0].data
fft_data = np.fft.fft(trace_data)
print(fft_data[:10])  # Print the first 10 elements of the FFT result #10 contoh sample pengambilan jumlah data
