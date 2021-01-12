처음부터 사용할 수 있는 방법:



Env 활성화

```
conda activate tf1-gpu-py36
```



데이터 전처리

```
python preprocess.py --num_workers 10 --name son --in_dir ./datasets/son --out_dir ./data/son

python preprocess.py --num_workers 10 --name moon --in_dir ./datasets/moon --out_dir ./data/moon
```



train_tacotron2.py, train_vocoder.py에 있는 default path 수정해주기:
load_path default=None 으로 해주기 (처음 돌리시)

