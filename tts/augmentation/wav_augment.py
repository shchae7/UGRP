import librosa.output
import numpy as np
import matplotlib.pyplot as plt


class AudioAugmentation:
    def read_audio_file(self, file_path):
        #input_length = 16000
        data = librosa.core.load(file_path)[0]
        #if len(data) > input_length:
        #    data = data[:input_length]
        #else:
        #    data = np.pad(data, (0, max(0, input_length - len(data))), "constant")
        return data

    def write_audio_file(self, file, data, sample_rate=22000):
        librosa.output.write_wav(file, data, sample_rate)


    def add_noise(self, data):
        noise = np.random.randn(len(data))
        data_noise = data + 0.005 * noise
        return data_noise

    def shift(self, data):
        return np.roll(data, 1600)

    def stretch(self, data, rate=1):
        #input_length = 16000
        data = librosa.effects.time_stretch(data, rate)
        #if len(data) > input_length:
        #    data = data[:input_length]
        #else:
        #    data = np.pad(data, (0, max(0, input_length - len(data))), "constant")
        return data

    def change_pitch(self, data):
        bins_per_octave = 12
        pitch_pm = 2
        pitch_change =  pitch_pm * 2*(np.random.uniform())
        data_pitch = librosa.effects.pitch_shift(data.astype('float64'), 22000, n_steps=pitch_change, bins_per_octave=bins_per_octave)
        return data_pitch
            

    def plot_time_series(self, data):
        plt.title('Raw wave ')
        plt.ylabel('Amplitude')
        plt.plot(np.linspace(0, 1, len(data)), data)
        plt.show()


# Create a new instance from AudioAugmentation class
augmenter = AudioAugmentation()

# Read and show cat sound
data = augmenter.read_audio_file("audio/origin.wav")

# Adding noise to sound
data_noise = augmenter.add_noise(data)

# Shifting the sound
data_roll = augmenter.shift(data)

# Stretching the sound
data_stretch = augmenter.stretch(data, 0.8)

# Changing the pith of the sound
data_pitch_change = augmenter.change_pitch(data)

# Write generated cat sounds
augmenter.write_audio_file('original_noise.wav', data)
augmenter.write_audio_file('noise_added.wav', data_noise)
augmenter.write_audio_file('noise_shifted.wav', data_roll)
augmenter.write_audio_file('noise_stretched.wav', data_stretch)
augmenter.write_audio_file('noise_pitch_changed.wav', data_pitch_change)