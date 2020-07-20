NVIDIA에서 제공한 공식적 Tacotron2, Waveglow 모델의 pretrained weight를 가지고 Google Colab에서 inference 할 수 있는 방법

Reference: https://jybaek.tistory.com/811

#Cell 1
import torch
waveglow = torch.hub.load('NVIDIA/DeepLearningExamples:torchhub', 'nvidia_waveglow')

#Cell 2
!pip install numpy scipy librosa unidecode inflect librosa

#Cell 3
import numpy as np
from scipy.io.wavfile import write

#Cell 4
waveglow = waveglow.remove_weightnorm(waveglow)
waveglow = waveglow.to('cuda')
waveglow.eval()

#Cell 5
tacotron2 = torch.hub.load('NVIDIA/DeepLearningExamples:torchhub', 'nvidia_tacotron2')
tacotron2 = tacotron2.to('cuda')
tacotron2.eval()

#Cell 6
text = "hello world, I missed you"

#Cell 7
# preprocessing
sequence = np.array(tacotron2.text_to_sequence(text, ['english_cleaners']))[None, :]
sequence = torch.from_numpy(sequence).to(device='cuda', dtype=torch.int64)

# run the models
with torch.no_grad():
    _, mel, _, _ = tacotron2.infer(sequence)
    audio = waveglow.infer(mel)
audio_numpy = audio[0].data.cpu().numpy()
rate = 22050

#Cell 8
from IPython.display import Audio
Audio(audio_numpy, rate=rate)

