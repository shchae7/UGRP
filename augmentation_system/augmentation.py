import librosa.output
import numpy as np
import sys
import matplotlib.pyplot as plt

USERID = 'shchae7'
OUTDIR = '/home/' + USERID + '/UGRP/tts/Tacotron2-Wavenet-Korean-TTS/datasets/son/audio/'

class AudioAugmentation:
    def __init__(self, file_path):
        self.data = librosa.core.load(file_path)[0]

    def write_audio_file(self, file, data, sample_rate=22000):
        librosa.output.write_wav(file, data, sample_rate)

    def add_noise(self):
        noise = np.random.randn(len(self.data))
        data_noise = self.data + 0.005 * noise
        return data_noise

    def shift(self):
        return np.roll(self.data, 1600)

    def stretch(self, rate=1):
        data = librosa.effects.time_stretch(self.data, rate)
        return data

    def change_pitch(self):
        bins_per_octave = 12
        pitch_pm = 2
        pitch_change =  pitch_pm * 2*(np.random.uniform())
        data_pitch = librosa.effects.pitch_shift(self.data.astype('float64'), 22000, n_steps=pitch_change, bins_per_octave=bins_per_octave)
        return data_pitch
            
    def plot_time_series(self, data):
        plt.title('Raw wave ')
        plt.ylabel('Amplitude')
        plt.plot(np.linspace(0, 1, len(data)), data)
        plt.show()



if __name__ == '__main__':
    dr = sys.argv[1]
    augmenter = AudioAugmentation(sys.argv[1])

    # Adding noise to sound
    data_noise = augmenter.add_noise()

    # Shifting the sound
    data_roll = augmenter.shift()

    # Stretching the sound
    data_stretch = augmenter.stretch(0.8)

    # Changing the pith of the sound
    data_pitch_change = augmenter.change_pitch()

    # Write generated cat sounds
    out_dir = '/home/' + USERID + '/UGRP/tts/Tacotron2-Wavenet-Korean-TTS/datasets/son/audio/'
    augmenter.write_audio_file(OUTDIR + sys.argv[2] + '_noise_added.wav', data_noise)
    augmenter.write_audio_file(OUTDIR + sys.argv[2] + '_noise_shifted.wav', data_roll)
    augmenter.write_audio_file(OUTDIR + sys.argv[2] + '_noise_stretched.wav', data_stretch)
    augmenter.write_audio_file(OUTDIR + sys.argv[2] + '_noise_pitch_changed.wav', data_pitch_change)