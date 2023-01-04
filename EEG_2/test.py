import numpy as np
import matplotlib.pyplot as plt
import aseegg as ag


czestotliwosc =5
t=np.linspace (0 ,1 ,250*1)
f=np.linspace (0 ,250 ,250*1)
sygnal=np.sin(2*np.pi*czestotliwosc*t)
transformata=ag.FFT(sygnal)


print(transformata[5])

plt.subplot (2,1,1)
plt.plot(t,sygnal)
plt.subplot (2,1,2)
plt.plot(f,transformata)
plt.show()

