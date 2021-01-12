# 실전 Slurm 사용법

## 0. 강두경이 찾아봐야 할거

1. --pty 의미
2. /bin/bash -l 의미
3. 생코에 질문 올렸는데 답변 좀 해주시면...

## 1. Slurm으로 파이썬 파일 실행하기

##### 1.1. 테스트 파이썬 파일 만들기

```bash
(base) [lapis@gpu-master ~]$ touch test.py
(base) [lapis@gpu-master ~]$ vim test.py
```

##### 1.2. test.py 수정하기

```python
print("Hello World")
```

Vim 저장할 때는 Esc 누른 후 Shift + z + z (ZZ)  입력하면 된다.

> vim 명령어 (https://opentutorials.org/course/730/4561) 
>
> "Esc"를 눌러야 명령어 모드로 바뀐다. 그 다음에 :(쉬트로+세미콜론키)을 누르고 명령어를 입력합니다.
> 명령어 설명 // [ ](각괄호)안의 글자는 생략해도 됩니다.
>
> **:w**[rite] 저장  // :(콜론)을 누른 다음에 w를 입력한 것입니다. :w # 처럼 숫자(#는 숫자입력을 표시)에 해당하는 파일 이름을 저장할 수 있다. 
> **:sav**[eas] #  // #(숫자를 의미)에 해당하는 파일을 '다른 이름'으로 저장한다.
> **:w** file.txt  // file.txt 파일로 저장
> **:w** » file.txt  // file.tx파일에 덧붙여서 저장
> **:q**  // vi 종료
> **:up**  // 바뀐 내용만 저장합니다.
> **:x**  // :upq와 같은 내용입니다.
> **:q!** // vi 강제 종료
> **ZZ** // 저장 후 종료
> **:wq!** // 강제 저장 후 종료
> **:e** file.txt file.txt파일을 불러옴
> **:e** 현재 파일을 불러옴
> **:e#** 바로 이전에 열었던 파일을 불러 옴

##### 1.3. 빠꾸없이 slurm으로 파이썬 파일 돌리기

```bash
(base) [lapis@gpu-master ~]$ srun python test.py
```

이러면 잠시 후 Hello World가 뜰 것이다. 저가 python test.py 들어갈 자리에 시간이 오래 걸리는 트레인 파일 실행 명령을 넣으면 된다!

## 2. Slurm으로 Shell 파일 실행하기

##### 2.1. Shell Script 만들기

```bash
$ touch test.sh
```

test.sh 파일을 만들고,

```bash
#!/bin/bash        
echo "Hello World 1"
echo "Hello World 2"
string_test() {
        echo "test"
}
string_test
```

  위와 같이 수정한다. shell script의 간단한 문법은 https://twpower.github.io/131-simple-shell-script-syntax 

##### 2.2. 사용 권한 지정

처음에 .sh 파일을 만들고 실행시키면 Permission Denied 가 뜰 수 있다. root 권한으로 만든 쉘이 아니면 그럴 수 있다. 이럴 땐 sudo나 chmod 등을 이용해 실행 권한을 일시적, 혹은 영구적으로 바꿔 주자.

```bash
$ chmod 744 test.sh
```



##### 2.3. 빠꾸없이 slurm으로 쉘스크립트 돌리기

아까랑 똑같이, 그냥 이렇게 명령을 입력하면 된다.

```bash
$ srun test.sh
Hello World 1
Hello World 2
test
```

##### 2.4. 1과 2를 합치면,

```bash
#!/bin/bash
python test.py
```

```bash
$ srun test.sh
Hello World
```

가 된다. 한 줄로 쓰기 어려운 시간이 오래 걸리는 명령은 Shell Script로 만들면 되겠지??

## 3. Slurm Options

##### 3.1. Command Line에서 바로 Option 바꾸기

| Option      | Expression                  |
| ----------- | --------------------------- |
| -J          | 작업 이름                   |
| -p          | 파티션 이름                 |
| -N          | 컴퓨팅 노드 수              |
| -n          | 필요한 프로세스 수          |
| -o          | stdout 파일 명 (작업이름.o) |
| -e          | stderr 파일 명(작업이름.e)  |
| --time      | 최대 작업 시간              |
| --gres=gpu: | 사용하는 gpu 카드 개수      |
| --pty       |                             |

##### 3.2. #SBATCH  사용하기

https://support.ceci-hpc.be/doc/_contents/QuickStart/SubmittingJobs/SlurmTutorial.html

For instance, hypothetically named submit.sh

```bash
#!/bin/bash
#
#SBATCH --job-name=test
#SBATCH --output=res.txt
#
#SBATCH --ntasks=1
#SBATCH --time=10:00
#SBATCH --mem-per-cpu=100

srun hostname
srun sleep 60
```

#SBATCH 옵션을 통해 이름을 설명할 수 있다.

```bash
$ sbatch submit.sh
```

위 스크립트를 실행해 보자. 아마 res.txt에 결과가 나올 것이다.(아마두?)

다른 옵션은 https://slurm.schedmd.com/srun.html 이거 보자.

## 4. Module 이용하여 작업

 커널에서 작업해야 하는 기능이 있는데 이를 추가하기 위해서는 커널을 수정해서 재컴파일해야 한다. 하지만 이는 너무 번거로우므로 리눅스와 같은 운영체제에서는 모듈이라는 기능을 제공하여 특정 커널의 기능을 사용하고자 할 때 실시간(동적)으로 추가할 수 있게 하고 있다.

출처: https://tribal1012.tistory.com/153 [Trillion]

...이라고 하는데, 그냥 모듈 올렸다 내렸다 해서 명령을 쓸 수 있거나 못 쓰거나 하게 할 수 있다. 그냥 자바스크립트나 파이썬 등등 스크립트 언어의 모듈이랑 비슷하다!

##### ml

현재 사용 가능한 모듈을 본다

##### ml purge

현재 사용 가능한 모듈을 모두 내린다.

##### ml av

load된 모듈의 디렉토리 상태(?)을 본다. 직접 써보면 이해됨.

(D) : Default Module, (L) : Module is Loaded

##### ml unload 모듈명, ml del 모듈명

현재 load된 모듈을 내린다(unload)

모듈이름이 cuda/9.2일 경우 모듈명에는 cuda를 넣어도 되고 cuda/9.2를 넣어도 된다.

##### ml swap 모듈명1 모듈명2

모듈1을 모듈2로 교체한다

##### ml spider

모듈이 서로 의존적으로 작동하는지를 확인한다(Dependencies)

##### ml save [이름]

현재 load된 모듈 목록을 저장한다.

##### ml sl

저장된 모듈 목록의 리스트를 출력한다.

##### ml restore

모듈 목록을 불러온다.

##### 예제(따라하면서 익히기)

```bash
$ ml purge
$ ml gnu7 cuda/9.2 cuDNN/cuda/9.2/7.6.4.38 python3/3.6.9 autotools cmake
$ ml save cuda9_2-cudnn7_6-py3_6
```

```bash
$ ml
$ ml purge
$ ml
$ ml autotools cuda/10.0 python3/3.6.9
$ ml
$ ml unload cuda
$ ml
$ ml av
$ ml swap python3/3.6.9 prun/1.3
$ ml
$ ml save test1
$ ml sl
$ ml purge
$ ml restore test1
$ ml
```



##### 주의사항

conda 환경에서 module 사용시 ml purge하자. python 충돌 주의.

## 5. Tensorflow Tutorial 갖다쓰기

##### 5.1. 클러스터의 Tutorial Script 복사하기

```bash
$ cp -r /opt/ohpc/pub/apps/SLURM-Batch-Training/ ~
$ cp -r /opt/ohpc/pub/apps/TensorFlow-2.x-Tutorials/ ~
```

다음으로, Single GPU node를 사용하는 텐서플로 스크립트를 보자.

```bash
cd SLURM-Batch-Training/01.GPU

cat tf-single-gpu-n1.sh

#!/bin/sh

#SBATCH -J  single-gpu           # Job name
#SBATCH -o  single-gpu.%j.out    # Name of stdout output file (%j expands to %jobId)
#SBATCH -t 01:30:00              # Run time (hh:mm:ss) - 1.5 hours

#SBATCH -p gpu-titanxp           # queue  name  or  partiton name  gpu-titanxp ,gpu-2080ti

#SBATCH   --gres=gpu:1

#SBATCH   --nodelist=n1
#SBATCH   --nodes=1
#SBATCH   --ntasks-per-node=1
#SBATCH   --cpus-per-task=1

cd  $SLURM_SUBMIT_DIR

echo "SLURM_SUBMIT_DIR=$SLURM_SUBMIT_DIR"
echo "CUDA_HOME=$CUDA_HOME"
echo "CUDA_VISIBLE_DEVICES=$CUDA_VISIBLE_DEVICES"
echo "CUDA_VERSION=$CUDA_VERSION"

srun -l /bin/hostname
srun -l /bin/pwd
srun -l /bin/date

module  purge
module  load  postech

SAMPLES_DIR=$HOME/TensorFlow-2.x-Tutorials/
python3  $SAMPLES_DIR/03-Play-with-MNIST/main.py

date

squeue  --job  $SLURM_JOBID


echo  "##### END #####"
```

이런 스크립트들이 여러개 있는데 설정 일부가 바뀐 게 다른 스크립트로 존재한다.



예를 들어 tf-2gpu.slurm.sh의 경우 두 개의 GPU를 사용한다. 

```bash
$ sbatch tf-2gpu.slurm.sh
```

이 명령을 여러 번 반복하고 squeue를 돌려보자. 아마 pending(PD 상태가 뜰 거다.)

아무튼 그렇다.

## 6. Tacotron 돌려보기

이제 우리는 슬럼을 배웠으니 이게 무슨 뜻인지 알 수 있다.

```bash
srun -N2 -n16 --ntasks=8 --time=1:00:00 --mem-per-cpu=2GB -o out.txt python train_tacotron2.py 
```

이렇게 한 번 돌려보자! 지금 finding for resources 뜬 상탠데 잘 하고 있는지 잘 모르겠당