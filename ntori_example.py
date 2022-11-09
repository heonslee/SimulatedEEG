import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.append('C:/workspace/codes-unsync/myGits/SimulatedEEG')
from ntori import ntori

ch = 3
tlen = 20
fs = 200
N = tlen*fs
del_org = 2*np.pi*np.random.rand(ch, 5000) - np.pi
delta = np.tile(del_org.reshape(ch, 5000, 1), (1,1,N))
# delta = np.array([del_org for _ in range(tlen*fs)])
f_tori = 100*np.random.rand(5000,1)
fm = 10

y, t = ntori(delta, fs, f_tori, fm)
plt.plot(t, y.T)
plt.xlim(0,10)
