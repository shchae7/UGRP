Dev Branch

# trigger_preprocess.py 실행에 관하여

<환경>
https://github.com/shchae7/UGRP/blob/docu/korean_tts_tf_env_setting_server_v0.md

<실행 (start from UGRP dir)>
시작 전 tts/Tacotron2-Wavenet-Korean-TTS/datasets/user/ 안에 audio 디렉터리를 만들어 주세요: mkdir audio

step 1: run the watchdog
```
cd tts/Tacotron2-Wavenet-Korean-TTS/
python triger_preprocess.py
```
step 2: move .wav files to datasets/user/audio dir
```
cd tts/Tacotron2-Wavenet-Korean-TTS/datasets/user
sh mv_wav.sh
```
step 3: check the result files (.npz, train.txt)
```
cd tts/Tacotron2-Wavenet-Korean-TTS/data/user
ls
```
