import numpy as np
import matplotlib.pyplot as plt

def unit_impulse(length, position):
    signal = np.zeros(length)
    # Ensure position is within bounds
    if 0 <= position < length:
        signal[position] = 1
    return signal

# Parameters
start = -10 # Start value of the x-axis range
stop = 10 # Stop value of the x-axis range
step = 1 # Step size

# Generate x-axis values
x = np.arange(start, stop+step, step)

# Calculate the position for the impulse at t=0
impulse_position = (0 - start) // step

# Generate unit impulse signal
impulse_signal = unit_impulse(len(x), impulse_position)

# Plot the signal
plt.stem(x, impulse_signal)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Unit Impulse Signal')
plt.grid(True)
plt.show()