과 서버에서 기본적인 개발 환경 setting하는 방법

Anaconda 설치

```
wget https://repo.anaconda.com/archive/Anaconda3-2019.10-Linux-x86_64.sh

sh Anaconda3-2019.10-Linux-x86_64.sh
```



필요한 env 생성

```
conda deactivate // 처음 상태는 (base)

conda create -n tf1-gpu-py36 python=3.6

conda activate tf1-gpu-py36 python=3.6
```



필요한 dependency 설치

```
pip install tensorflow-gpu==1.12.0 --user

pip install tqdm

pip install librosa

pip install unidecode

pip install inflect

pip install matplotlib
```

나중에 필요하면 requirements.txt 만들 예정