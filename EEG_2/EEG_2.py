import numpy as np
import matplotlib.pyplot as plt
import aseegg as ag
import pandas as pd

daneraw = np.genfromtxt('904.txt', delimiter=',')
def fft(dane):

    #38363 - 153,5s // 39924 159,5s
    dane = ag.pasmowozaporowy(dane[:,1],250,45,55) #Alicja2
    dane = ag.pasmowoprzepustowy(dane,250,6,32)
    fft = ag.FFT(dane)
    ag.rysujFFT(fft,250)


fft(daneraw)


#dane = ag.pasmowozaporowy(dane[:,0],250,45,55)
#dane = ag.pasmowoprzepustowy(dane,250,6,32)





#phase = dane[1400:3400]
#phase2 = dane[5250:7250]
#phase3 = dane[9000:11000]

#phasefft = ag.FFT(phase)
#phasefft = ag.FFT(phase2)
#phasefft = ag.FFT(phase3)

#mag = np.abs(phasefft)
#angle = np.angle(phasefft)

#fin = angle[np.argmax(mag)]

#print(mag)
#print(angle)
#print(fin)