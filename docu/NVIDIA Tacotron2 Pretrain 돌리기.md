# 1. NVIDIA Tacotron2 Pretrain 돌리기

## 1.1. 새 Conda 가상환경 만들기

### 1.1.1. Conda가 작동하나요?

```
$ conda
```

를 해 보고, conda not found가 뜬다면 conda가 제대로 설치되거나 세팅되지 않은 것!

### 1.1.2. 새 Conda 가상환경 만들고 conda library 설치하기

```bash
$ conda create -n te3 tensorflow python=3.6.8
$ conda activate te3
$ conda install tensorflow-gpu==1.15
```

 첫 줄의 te3 대신에는 자기가 넣고 싶은 environment의 이름을 넣자. 
 텐서플로우의 contrib attribute를 사용하기 위해 텐플 1.15를 설치한다.

## 2.1. pytorch 설치하기

### 2.1. pytorch  dependencies 설치하기

```bash
$ conda install -c pytorch magma-cuda100
$ conda install ninja pyyaml cmake mkl-include typing-extensions future
```

https://github.com/pytorch/pytorch#installation를 참고하면 어떻게 pytorch를 설치하는지 나와있다. 
최신 pytorch는 python 버전의 영향을 받지 않으므로 안심하고 깔면 된다.

### 2.2. pytorch 설치하기

```bash
$ git clone --recursive https://github.com/pytorch/pytorch
$ cd pytorch
$ git submodule sync
$ git submodule update --init --recursive
$ export CMAKE_PREFIX_PATH=${CONDA_PREFIX:-"$(dirname $(which conda))/../"}
$ python setup.py install
```

### 2.3. Apex 설치

 github에 나와있는 대로 소스를 다운받아서 apex를 설치하면 오류가 뜬다. 안전하게 conda-forge에서 apex를 설치하자.

```bash
$ conda install -c conda-forge nvidia-apex
```

## 3. 삽질

 github의 readme를 보면 이 다음 requirements.txt를 pip으로 모두 설치하라고 나와있는데, 이렇게 하면 numpy는 버전 오류가 생기고(이미 더 높은 버전의 numpy가 깔려있을 것이다) pillow를 제외한 나머지 모듈은 모두 버전에 맞게 설치되어 있다. 이렇게만 하면 될 줄 알았지만...

 생각보다 모듈을 까는 게 험난하고 내가 pip이랑 conda의 버전 관리나 어떻게 모듈을 가져오는지 정확히 잘 몰라 다음과 같이 모듈을 설치하는 과정에서 삽질을 많이 했다. 일단 이건 내가 history에서 가져온 건데, 설치하면서 y 계속 눌러주고 빨간 줄 뜨면 설치하라는 거 하나씩 설치하면서 해결해주자. 리잘알들은 삽질하지 말고 가장 효율적인 방법을 찾길 바란다... 전필 듣고 더욱 수련해서 오겠다 ㅠㅠ

 반드시 콘다 가상환경에서 돌려야 한다!

```bash
$ pip install pillow
$ pip install torchvision
$ pip install numba==0.48
$ pip install numpy==1.16.4
$ pip install decorator==3.4.2
$ pip install joblib
$ pip install scikit-learn
$ pip install tensorboard==1.15.0
$ pip install gast==0.2.2
$ pip install tensorflow-gpu==1.15
$ pip install tensorflow-estimator==1.15.1
$ pip install cycler python dateutil pytz
$ conda install pytorch==1.2.0 torchvision==0.4.0 -f https://download.pytorch.org/whl/torch_stable.html
$ conda install pytorch==1.2.0 torchvision==0.4.0 cudatoolkit=10.0 -c pytorch
```

### 3.1. pip list, conda list

나의 경우 모든 라이브러리 준비가 다 끝난 이후 pip list와 conda list는 다음과 같다.

pip list

```
absl-py                0.9.0
apex                   0.1
astor                  0.8.1
astunparse             1.6.3
attrs                  19.3.0
audioread              2.1.8
blinker                1.4
brotlipy               0.7.0
cachetools             4.1.0
certifi                2020.6.20
cffi                   1.14.0
chardet                3.0.4
click                  7.1.2
cryptography           2.9.2
cxxfilt                0.2.1
cycler                 0.10.0
decorator              3.4.2
future                 0.18.2
gast                   0.2.2
google-auth            1.17.2
google-auth-oauthlib   0.4.1
google-pasta           0.2.0
grpcio                 1.30.0
h5py                   2.10.0
idna                   2.10
importlib-metadata     1.7.0
inflect                0.2.5
iniconfig              1.0.1
joblib                 0.16.0
Keras-Applications     1.0.8
Keras-Preprocessing    1.1.2
librosa                0.6.0
llvmlite               0.31.0
Markdown               3.2.2
matplotlib             2.1.0
mkl-fft                1.1.0
mkl-random             1.1.1
mkl-service            2.3.0
more-itertools         8.4.0
numba                  0.48.0
numpy                  1.19.1
oauthlib               3.1.0
olefile                0.46
opt-einsum             3.1.0
packaging              20.4
Pillow                 7.2.0
pip                    20.1.1
pluggy                 0.13.1
protobuf               3.12.4
py                     1.9.0
pyasn1                 0.4.8
pyasn1-modules         0.2.7
pycparser              2.20
PyJWT                  1.7.1
pyOpenSSL              19.1.0
pyparsing              2.4.7
PySocks                1.7.1
pytest                 6.0.1
python-dateutil        2.8.1
pytz                   2020.1
PyYAML                 5.3.1
requests               2.24.0
requests-oauthlib      1.3.0
resampy                0.2.2
rsa                    4.0
scikit-learn           0.23.2
scipy                  1.0.0
setuptools             49.2.0.post20200714
six                    1.15.0
tensorboard            1.15.0
tensorboard-plugin-wit 1.6.0
tensorflow             1.15.2
tensorflow-estimator   1.15.1
tensorflow-gpu         1.15.0
termcolor              1.1.0
threadpoolctl          2.1.0
toml                   0.10.1
torch                  1.2.0+cu92
torchvision            0.4.0+cu92
tqdm                   4.48.2
typing-extensions      3.7.4.2
Unidecode              1.0.22
urllib3                1.25.9
webencodings           0.5.1
Werkzeug               1.0.1
wheel                  0.34.2
wrapt                  1.12.1
zipp                   3.1.0
```

conda list :

```
# packages in environment at /home/lapis/anaconda3/envs/te3:
#
# Name                    Version                   Build  Channel
_libgcc_mutex             0.1                        main
_pytorch_select           0.2                       gpu_0
_tflow_select             2.1.0                       gpu
absl-py                   0.9.0                    py36_0
astor                     0.8.0                    py36_0
astunparse                1.6.3                      py_0
attrs                     19.3.0                     py_0    conda-forge
blas                      1.0                         mkl
blinker                   1.4                      py36_0
brotlipy                  0.7.0           py36h7b6447c_1000
bzip2                     1.0.8                h7b6447c_0
c-ares                    1.15.0            h7b6447c_1001
ca-certificates           2020.6.24                     0
cachetools                4.1.0                      py_1
certifi                   2020.6.20                py36_0
cffi                      1.14.0           py36h2e261b9_0
chardet                   3.0.4                 py36_1003
click                     7.1.2                      py_0
cmake                     3.14.0               h52cb24c_0
cryptography              2.9.2            py36h1ba5d50_0
cudatoolkit               10.0.130                      0
cudnn                     7.6.5                cuda10.0_0
cupti                     10.0.130                      0
cxxfilt                   0.2.1            py36h831f99a_1    conda-forge
cycler                    0.10.0                   pypi_0    pypi
decorator                 3.4.2                    pypi_0    pypi
expat                     2.2.9                he6710b0_2
freetype                  2.10.2               h5ab3b9f_0
future                    0.18.2                   py36_1
gast                      0.2.2                    pypi_0    pypi
google-auth               1.17.2                     py_0
google-auth-oauthlib      0.4.1                      py_2
google-pasta              0.2.0                      py_0
grpcio                    1.27.2           py36hf8bcb03_0
h5py                      2.10.0           py36hd6299e0_1
hdf5                      1.10.6               hb1b8bf9_0
idna                      2.10                       py_0
importlib-metadata        1.7.0            py36h9f0ad1d_0    conda-forge
importlib_metadata        1.7.0                         0    conda-forge
iniconfig                 1.0.1              pyh9f0ad1d_0    conda-forge
intel-openmp              2020.1                      217
joblib                    0.16.0                   pypi_0    pypi
jpeg                      9b                   h024ee3a_2
keras-applications        1.0.8                      py_1
keras-preprocessing       1.1.0                      py_1
krb5                      1.18.2               h173b8e3_0
lcms2                     2.11                 h396b838_0
libcurl                   7.71.1               h20c2e04_1
libedit                   3.1.20191231         h14c3975_1
libffi                    3.2.1                hd88cf55_4
libgcc-ng                 9.1.0                hdf63c60_0
libgfortran-ng            7.3.0                hdf63c60_0
libpng                    1.6.37               hbc83047_0
libprotobuf               3.12.3               hd408876_0
libssh2                   1.9.0                h1ba5d50_1
libstdcxx-ng              9.1.0                hdf63c60_0
libtiff                   4.1.0                h2733197_1
llvmlite                  0.31.0                   pypi_0    pypi
lz4-c                     1.9.2                he6710b0_1
magma-cuda100             2.5.2                         1    pytorch
markdown                  3.1.1                    py36_0
mkl                       2020.1                      217
mkl-include               2020.1                      217
mkl-service               2.3.0            py36he904b0f_0
mkl_fft                   1.1.0            py36h23d657b_0
mkl_random                1.1.1            py36h0573a6f_0
more-itertools            8.4.0                      py_0    conda-forge
ncurses                   6.2                  he6710b0_1
ninja                     1.10.0           py36hfd86e86_0
numba                     0.48.0                   pypi_0    pypi
numpy                     1.16.4                   pypi_0    pypi
numpy-base                1.19.1           py36hfa32c7d_0
nvidia-apex               0.1              py36h8d9616a_1    conda-forge
oauthlib                  3.1.0                      py_0
olefile                   0.46                     py36_0
openssl                   1.1.1g               h516909a_1    conda-forge
opt_einsum                3.1.0                      py_0
packaging                 20.4               pyh9f0ad1d_0    conda-forge
pillow                    7.2.0            py36hb39fc2d_0
pip                       20.1.1                   py36_1
pluggy                    0.13.1           py36h9f0ad1d_2    conda-forge
protobuf                  3.12.3           py36he6710b0_0
py                        1.9.0              pyh9f0ad1d_0    conda-forge
pyasn1                    0.4.8                      py_0
pyasn1-modules            0.2.7                      py_0
pycparser                 2.20                       py_2
pyjwt                     1.7.1                    py36_0
pyopenssl                 19.1.0                     py_1
pyparsing                 2.4.7              pyh9f0ad1d_0    conda-forge
pysocks                   1.7.1                    py36_0
pytest                    6.0.1            py36h9f0ad1d_0    conda-forge
python                    3.6.8                h0371630_0
python-dateutil           2.8.1                    pypi_0    pypi
python_abi                3.6                     1_cp36m    conda-forge
pytorch                   1.2.0           py3.6_cuda10.0.130_cudnn7.6.2_0    pytorch
pytz                      2020.1                   pypi_0    pypi
pyyaml                    5.3.1            py36h7b6447c_1
readline                  7.0                  h7b6447c_5
requests                  2.24.0                     py_0
requests-oauthlib         1.3.0                      py_0
rhash                     1.3.8                h1ba5d50_0
rsa                       4.0                        py_0
scikit-learn              0.23.2                   pypi_0    pypi
scipy                     1.5.0            py36h0b6359f_0
setuptools                49.2.0                   py36_0
six                       1.15.0                     py_0
sqlite                    3.32.3               h62c20be_0
tensorboard               1.15.0             pyhb230dea_0
tensorboard-plugin-wit    1.6.0                      py_0
tensorflow                1.15.0          gpu_py36h5a509aa_0
tensorflow-base           1.15.0          gpu_py36h9dcbed7_0
tensorflow-estimator      1.15.1             pyh2649769_0
tensorflow-gpu            1.15.0                   pypi_0    pypi
termcolor                 1.1.0                    py36_1
threadpoolctl             2.1.0                    pypi_0    pypi
tk                        8.6.10               hbc83047_0
toml                      0.10.1             pyh9f0ad1d_0    conda-forge
torch                     1.2.0+cu92               pypi_0    pypi
torchvision               0.4.0+cu92               pypi_0    pypi
tqdm                      4.48.2             pyh9f0ad1d_0    conda-forge
typing-extensions         3.7.4.2                       0
typing_extensions         3.7.4.2                    py_0
urllib3                   1.25.9                     py_0
webencodings              0.5.1                    py36_1
werkzeug                  0.16.1                     py_0
wheel                     0.34.2                   py36_0
wrapt                     1.12.1           py36h7b6447c_1
xz                        5.2.5                h7b6447c_0
yaml                      0.2.5                h7b6447c_0
zipp                      3.1.0                      py_0    conda-forge
zlib                      1.2.11               h7b6447c_3
zstd                      1.4.5                h9ceee32_0
```



## 4. pretrain 준비

### 4.1. tacotron2 받기

```bash
$ git clone https://github.com/NVIDIA/tacotron2.git
$ cd tacotron2
$ git submodule init
$ git submodule update
$ wget https://data.keithito.com/data/speech/LJSpeech-1.1.tar.bz2
$ tar -xf LJSpeech-1.1.tar.bz2
$ rm LJSpeech-1.1.tar.bz2
$ sed -i -- 's,DUMMY,LJSpeech-1.1/wavs,g' filelists/*.txt
```

다음으로, tacotron2의 hparams.py의 디렉토리를 절대 경로로 변경해주어야 한다. (두 개 변경해주면 된다.)

28, 29번째 줄을 예를 들어 이렇게 바꿔주자.

```python
...
training_files='/home/lapis/tacotron2/filelists/ljs_audio_text_train_filelist.txt'
validation_files='/home/lapis/tacotron2/filelists/ljs_audio_text_val_filelist.txt'
...
```

그다음 또 문제가 있다. 아마 이대로 쭉 해서 슬럼 배치를 실행하면 code is too big 오류가 뜰 수도 있다. 원래 안 떠야 정상인데, 나는 뜨는데 다음과 같은 방법으로 수정할 수 있다.

stft.py의 91번째 줄부터 다음과 같이 바꿔주자.

```python
forward_transform = F.conv1d(
            input_data.cuda(),
            Variable(self.forward_basis, requires_grad=False).cuda(),
            stride=self.hop_length,
            padding=0).cpu()
```



### 4.2. 데이터셋 받기

https://drive.google.com/file/d/1c5ZTuT7J08wLUoVZ2KkUs_VdZuJ86ZqA/view 에서 데이터셋을 받은 이후, 서버로 올려줘야 한다. 서버로 올릴 때는 scp를 이용하자. 

로컬 터미널에서 scp [source] [dest]를 해 주면 된다.

```powershell
C:\Users\stkd3\Desktop> scp tacotron2_statedict.pt lapis@csecluster.postech.ac.kr:/home/lapis/tacotron2
```

예를 들어 이런 식으로. 내 파일이 바탕화면에 있다면 이렇게 하면 된다.

### 4.3. slurm batch file 작성

```sh
#!/bin/sh

#SBATCH -J pretrain
#SBATCH -p gpu-2080ti-8
#SBATCH -t 24:00:00
#SBATCH --gres=gpu:1
#SBATCH --nodelist=n17

echo "Start Pre-Train"
echo "SLURM_SUBMIT_DIR = $SLURM_SUBMIT_DIR"
echo "CUDA_HOME = $CUDA_HOME"
echo "CUDA_VISIBLE_DEVICES = $CUDA_VISIBLE_DEVICES"
echo "CUDA_VERSION=$CUDA_VERSION"


srun -l /bin/hostname
srun -l /bin/pwd
srun -l /bin/date

conda init bash
conda activate te3

python train.py --output_directory=$HOME/out --log_directory=$HOME/out -c $HOME/tacotron2/tacotron2_statedict.pt --warm_start
date
conda deactivate
squeue --job $SLURM_JOBID
echo "####end####"
~                    
```

를 command.sh라는 파일명으로 작성해서 tacotron2 파일에 넣었다.

물론 다른 분들이 실행할 때는 sbatch -p, --gres 옵션을 다르게 해도 좋다! 

파일을 수정할 때는 vim을 사용한다. vim 사용법을 참고하길 바란다.

### 4.4. Pretrain 돌리기

간단히 그냥 

```bash
$ sbatch command.sh
```

를 돌리고, squeue를 하면서 기다려보자. output은 slurm-xxxxx.out 파일에 나올테니까 그걸 보면서 뭐가 문제였는지를 캐치해보자.

만약 train이 잘 돌아가는 것 같다! squeue를 했는데 내가 방금 올린 슬럼 작업이 계속 RUNNING이 뜬다! 그러면 24시간(위 command.sh에서 24시간으로 설정했다) 이후에 다시 확인해보자...

## 5. 주의사항

### 5.1. 반드시 conda 가상환경에서 실행되는지 확인하자.

conda 가상환경에서 실행되는지 확인해야 한다. 일례로 저 sbatch를 한번 돌리고 나면 conda 가상환경 설정이 해제되기 때문에 다시 activate해줘야 한다. 내가 그거 깜빡하고 모듈 언인스톨하려다가 큰일날뻔한 적이 있다.

### 5.2. 로그인했더니 .bashrc가 바뀌어 있어요...

행여나 conda 명령을 입력했는데 conda를 못 찾는다면? 처음 ssh를 켰는데 다음과 같은 에러줄이 뜬다면?

```bash
-bash: /home/lapis/.bashrc: line 21: syntax error near unexpected token `else'
-bash: /home/lapis/.bashrc: line 21: `    else'
```

내가 그렇다. 어떤 저주에 걸려버린건지는 모르겠지만 나는 채승현이 내 아이디로 자기 맥북에서 로그인한번 한 후로 로그인할때마다 .bashrc가 바뀌는 저주에 걸렸다.

**vim .bashrc로 .bashrc 파일을 열어보면 if, else 다음 구문 줄이 주석 처리 되어 있는 걸 볼 수 있다. 그 주석 처리를 해제한 후** 

```bash
$ source .bashrc
```

로 .bashrc를 실행시켜서 다시 conda를 activate 시키도록 하자. 이 문제는 구글링하면 해결법이 나올 거 같긴 하다.

### 5.3. 이 외에도...

No CUDA-Capable device : 슬럼에서 돌리는 게 아니라면 GPU와 통신할 수 없다. 일례로 그냥 nvidia-smi를 실행하면 실패했다고 뜨지만, slurm 환경에서 nvidia-smi를 실행하면 가슴이 웅장해지는 gpu 관련 정보를 열람할 수 있을 것이다.

*.so.2 file 안보임~~, numpy 못찾음  등등 : 콘다에서 돌리자. 한번 더 돌리자

어쩌면 그냥 내 아이디와 비번을 공유하는게 맞을지도 모르겠다. 과클러스터 메모리 낭비아닌가 싶기도 하네.
