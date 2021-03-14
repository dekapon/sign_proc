from scipy.io import wavfile
import matplotlib.pyplot as plt
import numpy as np

print(f'Hello world homework 1 ex 1')

# 1.1
def uniform_quantization(inputSig, min_amplitude, max_amplitude, quantization_levels):
    to_values = np.linspace(min_amplitude, max_amplitude, quantization_levels)
    outputSig = [0] * inputSig.size

    for i in range(inputSig.size):
        best_match = None
        best_match_diff = None
        for other_val in to_values:
            diff = abs(other_val - inputSig[i])
            if best_match is None or diff < best_match_diff:
                best_match = other_val
                best_match_diff = diff
            outputSig[i] = best_match
    return outputSig

# 1.2
f = 0.2  # value in Hz (default is 1)
duration = 5  # s
fs = 500  # sampling rate in Hz
A = 1
x = np.linspace(0, duration, duration * fs)
y = A * np.sin(2 * np.pi * f * x)
min_amplitude = -1
max_amplitude = 1

n = x.size
m = 3
quantSin = [[0] * m for i in range(m)]
plt.plot(x, y)
for i in range(m):
    if i == 0:
        quantization_levels = 2
    elif i == 1:
        quantization_levels = 4
    elif i == 2:
        quantization_levels = 16
    quantSin[i] = uniform_quantization(y, min_amplitude, max_amplitude, quantization_levels)
    plt.plot(x, quantSin[i])

    # plt.ax.plot([1, 2, 3])
    # plt.ax.legend(['A simple line'])
plt.legend(["Sine", "2 levels quant.", "4 levels quant.", "16 levels quant."])
plt.show()

# 1.3
