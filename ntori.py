import numpy as np


def ntori(delta, fs, f_tori, fm):
    ch, _, N = delta.shape
    t = np.linspace(0, N/fs-1/fs, N)
    x = 2*np.pi*f_tori*t
    x = x + delta
    f_tori /= fm
    
    amp = np.sqrt(np.pi*f_tori/2)*np.exp(-np.pi*(f_tori**2)/4)
    y = amp.reshape(1,5000,1)*np.sin(x)
    y = y.sum(1)
    return y, t



