Dev Branch
# trigger_script_proceed.sh 실행에 관하여
<환경>
tacotron2와 wavenet의 training이 정상적으로 돌아가는 tf1-gpu-py36과 tf2-gpu-py36 conda environment를 미리 만들어놓기를 추천합니다. 

<가정>
`UGRP/script/server` 에서 script_all.txt 로 스크립트를 만들어두고, script_split.py의 실행으로 script_line에 script_line이 저장되어 있음을 가정합니다. 

<실행>
step 1: local에서 download watchdog 실행합니다. 
```
[local: UGRP/script/computer]$ python sc_script_download_wd.py
```
step 2: server에서 trigger_script_proceed.sh 실행합니다. 
```
[server: UGRP/tts/Tacotron2-Wavenet-Korean-TTS]$ sh trigger_script_proceed.sh
```
step 3: local의 upload watchdog 실행합니다. 
```
[local: UGRP/script/computer]$ python cs_script_upload_wd.py
```
step 4: local의 computer/upload 폴더에 wav 파일 추가(현재는 0000001 ~ 000004, 4개)
```
[local: UGRP/script/computer]$ cp recorded/script_0000001.wav upload
[local: UGRP/script/computer]$ cp recorded/script_0000002.wav upload
[local: UGRP/script/computer]$ cp recorded/script_0000003.wav upload
[local: UGRP/script/computer]$ cp recorded/script_0000004.wav upload
```
step 5: step 2의 shell script가 종료되면, squeue를 통해 제대로 training되고 있는지 한 번 확인해줍니다. 
```
[server: UGRP/tts/Tacotron2-Wavenet-Korean-TTS]$ squeue
JOBID  NAME          STATE     USER     GROUP    PARTITION       NODE NODELIST CPUS TRES_PER_NODE TIME_LIMIT  TIME_LEFT  
1175   KTacoTr       RUNNING   parksbn8 usercl   titanxp         1    n3       1    gpu:2         2:00:00     1:17:25    
1176   KWaveTr       RUNNING   parksbn8 usercl   titanxp         1    n4       1    gpu:2         2:00:00     1:17:25  
```
step 6: 생성된 endfile을 local로 다운합니다. 
```
[local: UGRP/script/computer]$ python sc_script_download_wd.py
```

# trigger_preprocess.py 실행에 관하여

<환경>
cse-cluster1에서 base 환경에 다음 문서의 가장 아래 text box에 있는 모듈들을 설치하면 정상적으로 실행됩니다.
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
