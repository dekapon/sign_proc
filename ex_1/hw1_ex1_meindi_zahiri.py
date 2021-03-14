from scipy.io import wavfile
import soundfile as sf
import matplotlib.pyplot as plt
import numpy as np
import time

print(f'Hello world homework 1 ex 1')
test = 1 # put to 0 before sending assignment
t = time.time()

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
quantSin = [[0] * m for i in range(n)]
plt.plot(x, y)
quantization_levels = [2, 4, 16]
for i in range(m):
    quantSin[i] = uniform_quantization(y, min_amplitude, max_amplitude, quantization_levels[i])
    plt.plot(x, quantSin[i])

    # plt.ax.plot([1, 2, 3])
    # plt.ax.legend(['A simple line'])
plt.legend(["Sine", "2 levels quant.", "4 levels quant.", "16 levels quant."])
plt.show()

# 1.3
# samplerate, audioIn = wavfile.read('peter.wav')
audioIn, samplerate = sf.read('peter.wav')

if test:
    bitsDepth = [2, 3, 4]
else:
    """
    It doesnt work with 16, it takes too long to compute, but i checked the audio file 
    and it seems to be already 16 bits depth.
    
    So i put 8 bits depth instead of 16, execution time goes from 2.5s to 16s.
    
    When i profile my code, i see that the program is spending 96% of the time in 
    my uniform quantization function, because i iterate through a large array 
    for the comparison with each sample.
    """
    bitsDepth = [2, 4, 8]

quantization_levels = len(bitsDepth) * [0]

timeInterval = [0.5, 0.51]
samplePos = [samplerate * timeInterval[0], samplerate * timeInterval[1]]
# print(samplePos)
samplePos = [int(item) for item in samplePos]  # items in the list are float, so i convert them to int


plt.figure()
x = np.linspace(0, audioIn.size, audioIn.size)
plt.plot(x[samplePos[0]:samplePos[1]], audioIn[samplePos[0]:samplePos[1]])
m = len(bitsDepth)
quantAudio = [[0] * m for i in range(n)]

min_amplitude = min(audioIn[samplePos[0]:samplePos[1]])
max_amplitude = max(audioIn[samplePos[0]:samplePos[1]])
# print(str(min_amplitude) + "   " + str(max_amplitude))
for i in range(len(bitsDepth)):
    quantization_levels[i] = 2 ** bitsDepth[i]
    quantAudio[i] = uniform_quantization(audioIn, min_amplitude, max_amplitude, quantization_levels[i])
    plt.plot(x[samplePos[0]:samplePos[1]], quantAudio[i][samplePos[0]:samplePos[1]])
    # wavfile.write("peter_" + str(bitsDepth[i]) + " bits depth.wav",samplerate,quantAudio[i])
    sf.write("peter_" + str(bitsDepth[i]) + " bits depth.wav",quantAudio[i],samplerate)
plt.legend(["original audio", "2 bits depth quant.", "4 bits depth quant.", "8 bits depth quant."])
plt.show()
# print(quantAudio[1])
# sf.write('new_file.flac', data, samplerate)

elapsed = time.time() - t
print("done, elapsed time: " + str(elapsed) + " s")



