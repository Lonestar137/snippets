import numpy as np
import matplotlib.pyplot as plt

# Parameters
amplitude = 1.0  # Amplitude of the sine wave
frequency = 1.0  # Frequency of the sine wave
duration = 5.0  # Duration of the sine wave in seconds
sampling_rate = 1000  # Number of samples per second

# Calculate time values
t = np.linspace(0, duration, int(duration * sampling_rate), endpoint=False)

# Generate the sine wave
waveform = amplitude * np.sin(2 * np.pi * frequency * t)

# Plot the sine wave
plt.plot(t, waveform)
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Sine Wave")
plt.show()
