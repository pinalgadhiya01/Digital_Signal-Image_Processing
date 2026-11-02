import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, cheby1, sosfiltfilt

# Step 1: Define parameters
Fs = 8000                  # Sampling frequency
duration = 0.05            # Signal duration
t = np.arange(0, duration, 1/Fs)

# Step 2: Generate four sine waves
f1 = 1000
f2 = 2000
f3 = 3000
f4 = 4000

signal1 = np.sin(2 * np.pi * f1 * t)
signal2 = np.sin(2 * np.pi * f2 * t)
signal3 = np.sin(2 * np.pi * f3 * t)
signal4 = np.cos(2 * np.pi * f4 * t)

# Step 3: Plot all four individual signals
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.plot(t, signal1)
plt.title('1 KHz Sine Wave')
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')
plt.grid()

plt.subplot(2, 2, 2)
plt.plot(t, signal2)
plt.title('2 KHz Sine Wave')
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')
plt.grid()

plt.subplot(2, 2, 3)
plt.plot(t, signal3)
plt.title('3 KHz Sine Wave')
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')
plt.grid()

plt.subplot(2, 2, 4)
plt.plot(t, signal4)
plt.title('4 KHz Signal')
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')
plt.grid()

plt.tight_layout()
plt.show()

# Step 4: Add all four signals
combined_signal = signal1 + signal2 + signal3 + signal4

# Function to plot frequency spectrum
def plot_frequency(signal, title):

    N = len(signal)

    frequency = np.fft.rfftfreq(N, 1/Fs)

    spectrum = np.abs(np.fft.rfft(signal)) / N

    plt.figure(figsize=(10, 5))
    plt.plot(frequency, spectrum)

    plt.title(title)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude')
    plt.grid()
    plt.tight_layout()
    plt.show()


# Step 5: Plot combined signal in time domain
plt.figure(figsize=(10, 5))
plt.plot(t, combined_signal)

plt.title('Combined Signal in Time Domain')
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')
plt.grid()
plt.tight_layout()
plt.show()

# Step 6: Plot combined signal in frequency domain
plot_frequency(combined_signal,
               'Combined Signal in Frequency Domain')


# Step 7: Design Butterworth Low-Pass Filter
filter_order = 4
butter_cutoff = 2000

butter_filter = butter(
    filter_order,
    butter_cutoff,
    btype='lowpass',
    fs=Fs,
    output='sos'
)

# Apply Butterworth filter
butter_output = sosfiltfilt(
    butter_filter,
    combined_signal
)

# Step 8: Plot Butterworth output in time domain
plt.figure(figsize=(10, 5))
plt.plot(t, butter_output)

plt.title('Butterworth Filter Output - Time Domain')
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')
plt.grid()
plt.tight_layout()
plt.show()

# Step 9: Plot Butterworth output in frequency domain
plot_frequency(butter_output,
               'Butterworth Filter Output - Frequency Domain')


# Step 10: Design Chebyshev Low-Pass Filter
cheby_cutoff = 3000
ripple = 0.5

cheby_filter = cheby1(
    filter_order,
    ripple,
    cheby_cutoff,
    btype='lowpass',
    fs=Fs,
    output='sos'
)

# Apply Chebyshev filter
cheby_output = sosfiltfilt(
    cheby_filter,
    combined_signal
)

# Step 11: Plot Chebyshev output in time domain
plt.figure(figsize=(10, 5))
plt.plot(t, cheby_output)

plt.title('Chebyshev Filter Output - Time Domain')
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')
plt.grid()
plt.tight_layout()
plt.show()

# Step 12: Plot Chebyshev output in frequency domain
plot_frequency(cheby_output,
               'Chebyshev Filter Output - Frequency Domain')

print("All signals generated successfully!")
print("Butterworth and Chebyshev filtering completed!")
