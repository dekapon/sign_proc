from scipy.io import wavfile
import matplotlib.pyplot as plt
import numpy as np

print(f'Hello world homework 1 ex 1')


def quantize(val, to_values):
    """Quantize a value with regards to a set of allowed values.

    Examples:
        quantize(49.513, [0, 45, 90]) -> 45
        quantize(43, [0, 10, 20, 30]) -> 30

    Note: function doesn't assume to_values to be sorted and
    iterates over all values (i.e. is rather slow).

    Args:
        val        The value to quantize
        to_values  The allowed values
    Returns:
        Closest value among allowed values.
    """
    best_match = None
    best_match_diff = None
    for other_val in to_values:
        diff = abs(other_val - val)
        if best_match is None or diff < best_match_diff:
            best_match = other_val
            best_match_diff = diff
    return best_match

def uniform_quantization(audio_sig, min_amplitude, max_amplitude, quantization_levels):
    # a = int(a)
    # b = int(b)
    # c = int(c)
    # x = np.linspace(a, b, c)
    # if a >= 0 and b >= 0:
    #     y = np.arctan(np.tan(2 * math.pi * x))
    #     plt.plot(x, y)

    ownDigitize = 3
    audioOut = [0] * audio_sig.size
    if ownDigitize == 1: # my quant
        q = 2 / quantization_levels
        bits = int(np.sqrt(quantization_levels))
        print(q)
        for i in range(audio_sig.size):
            # audioOut[i] = round(audioIn[i] * 2 ** (bits - 1) / 2 ** (bits - 1) - np.sign(audioIn[i] * q / 2), 2)))
            # audioOut[i] = round(audioIn[i] * 2 ** (bits - 1) / 2 ** (bits - 1) - np.sign(audioIn[i] * q / 2), 2)))
            # audioOut[i] = (round(audioIn[i] * 2 ** (bits - 1) / (2 ** (bits-1)), 2) - np.sign(audioIn[i]) * q /2)
            audioOut[i] = round((audio_sig[i] * 2 ** (bits - 1)) / 2 ** (bits - 1))
            audioOut[i] = audioOut[i] - (np.sign(audio_sig[i]) * q / 2)
            if audioOut[i] < min_amplitude:
                audioOut[i] = min_amplitude
            elif audioOut[i] > max_amplitude:
                audioOut[i] = max_amplitude
            # audioOut[i] /= 2
    elif ownDigitize == 2: # tim quant
        q = 2 / quantization_levels
        # quantization_steps =np.linspace(min_amplitude, max_amplitude, q)
        # quantization_steps =np.round(np.linspace(min_amplitude, max_amplitude, quantization_levels, endpoint = True))
        quantization_steps = np.linspace(min_amplitude, max_amplitude, quantization_levels)
        print(quantization_steps)
        bins = np.digitize(audio_sig, quantization_steps, right=True)
        print(bins)

        # audioOut = bins * quantization_steps
        for i in range(audio_sig.size):
            audioOut[i] = quantization_steps[bins[i]]
    elif ownDigitize == 3: # internet quant
        q = 2 / quantization_levels
        quantization_steps = np.linspace(min_amplitude, max_amplitude, quantization_levels)
        print(quantization_steps)
        bins = np.digitize(audio_sig, quantization_steps, right=True)
        print(bins)

        # audioOut = bins * quantization_steps
        for i in range(audio_sig.size):
            audioOut[i] = quantize(audioIn[i], quantization_steps)
    return audioOut


samplerate, audioIn = wavfile.read('peter.wav')
sine = 1
if sine:
    audioIn = np.sin(np.linspace(1, audioIn.size, audioIn.size))
else:
    quantization_levels = 4
    min_amplitude = np.min(audioIn)
    max_amplitude = np.max(audioIn)
    print(min_amplitude)
    print(max_amplitude)
    audioOut = uniform_quantization(audioIn, min_amplitude, max_amplitude, quantization_levels)

# x = np.linspace(1, audioIn.size, 1)
x = np.linspace(1, audioIn.size, audioIn.size)
# print(np.min(audioIn))
test = audioIn[20000:20050]
zoom = 3
if zoom == 1:  # zoomed
    plt.plot(np.linspace(20000, 20050), audioIn[20000:20050])
    plt.plot(np.linspace(20000, 20050), audioOut[20000:20050])
    # plt.plot(x, audioOut)
elif zoom == 2:  # not zoomed
    plt.plot(x, audioIn)
    plt.plot(x, audioOut)
elif zoom == 3:  # sine function
    f = 0.20  # value in Hz
    duration = 5  # s
    fs = 500  # sampling rate in Hz
    A = 1
    x = np.linspace(0, duration, duration * fs)
    # for i in range(x.size)
    # y[i] = A * np.sin(2 * np.pi * f * x)
    y = A * np.sin(2 * np.pi * f * x)
    # f(t) = A sin(2*pi*f*t + phi)
    plt.plot(x, y)
    min_amplitude = -1
    max_amplitude = 1
    quantization_levels = 8
    sine_quant = uniform_quantization(y, min_amplitude, max_amplitude, quantization_levels)

    plt.plot(x, sine_quant)
plt.show()
