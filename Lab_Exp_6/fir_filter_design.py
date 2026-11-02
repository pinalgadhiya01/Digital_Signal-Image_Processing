import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, freqz

# Step 1: Define filter parameters
Fs = 20000       # Sampling frequency = 20 KHz
Fc = 3000        # Cutoff frequency = 3 KHz
N = 31           # Number of filter taps

# Step 2: Design FIR Low-Pass Filter
lpf = firwin(
    numtaps=N,
    cutoff=Fc,
    window='hann',
    pass_zero='lowpass',
    fs=Fs
)

# Step 3: Design FIR High-Pass Filter
hpf = firwin(
    numtaps=N,
    cutoff=Fc,
    window='hann',
    pass_zero='highpass',
    fs=Fs
)

# Step 4: Design FIR Band-Pass Filter
bpf = firwin(
    numtaps=N,
    cutoff=[3000, 6000],
    window='hann',
    pass_zero='bandpass',
    fs=Fs
)

# Step 5: Design FIR Band-Stop Filter
bsf = firwin(
    numtaps=N,
    cutoff=[3000, 6000],
    window='hann',
    pass_zero='bandstop',
    fs=Fs
)

# Step 6: Calculate frequency response
filters = [
    (lpf, 'FIR Low-Pass Filter'),
    (hpf, 'FIR High-Pass Filter'),
    (bpf, 'FIR Band-Pass Filter'),
    (bsf, 'FIR Band-Stop Filter')
]

# Step 7: Plot all four graphs separately
for b, title in filters:

    f, H = freqz(b, worN=2048, fs=Fs)

    magnitude_db = 20 * np.log10(
        np.maximum(np.abs(H), 1e-10)
    )

    plt.figure(figsize=(10, 5))

    plt.plot(f, magnitude_db)

    plt.title(title + ' using Hann Window')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude (dB)')

    plt.grid(True)
    plt.tight_layout()
    plt.show()
