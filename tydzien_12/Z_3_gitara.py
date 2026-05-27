#!/usr/bin/python3

import os

import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile
import scipy.fft
import scipy.signal

katalog_nadrzedny = os.path.dirname(__file__)
probkowanie, dane = scipy.io.wavfile.read(os.path.join(katalog_nadrzedny, 'gitara.wav'))

print(probkowanie)
print(dane)

dlugosc_dzwieku = len(dane)/probkowanie

print(dlugosc_dzwieku)

fourier = scipy.fft.fft(dane)
czestotliwosci = scipy.fft.fftfreq(len(fourier), 1/probkowanie)

piki, info = scipy.signal.find_peaks(np.abs(fourier)[:len(fourier)//2], height=3e6)

# print(piki)
# print(info)

czasy = np.linspace(0, dlugosc_dzwieku, len(dane))

fig, ax = plt.subplots()

ax.plot(czestotliwosci[:len(fourier)//2], np.abs(fourier)[:len(fourier)//2])
ax.plot(czestotliwosci[:len(fourier)//2][piki], info['peak_heights'], 'rx')
print(czestotliwosci[:len(fourier)//2][piki])

ax.set_xlim(0, 5000)

for pik, wys in zip(czestotliwosci[:len(fourier)//2][piki], info['peak_heights']):
    ax.text(pik, wys, f'$f={round(pik)}$ Hz', horizontalalignment='center', verticalalignment='bottom')

ax.set_xlabel('$f$ (Hz)')
ax.set_ylabel('Fourier')

plt.show()
plt.close(fig)
