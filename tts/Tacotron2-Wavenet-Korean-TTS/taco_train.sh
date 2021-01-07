#!/bin/sh

#SBATCH -J KTacoTr
#SBATCH -o ./out_files/KTacoTr.%j.out
#SBATCH -p titanxp
#SBATCH -t 02:00:00
#SBATCH --gres=gpu:2

echo "Start Training Korean Tacotron2"
echo "SLURM_SUBMIT_DIR = $SLURM_SUBMIT_DIR"
echo "CUDA_HOME = $CUDA_HOME"
echo "CUDA_VISIBLE_DEVICES = $CUDA_VISIBLE_DEVICES"
echo "CUDA_VERSION=$CUDA_VERSION"

srun -l /bin/hostname
srun -l /bin/pwd
srun -l /bin/date

conda init bash
conda activate tf1-gpu-py36

while getopts "u:" opt; do
  case $opt in
    u)
      echo >&2 "-u was triggered!, OPTARG: $OPTARG"
      if [ $OPTARG == "user" ]
      then
        python tacotron2_train.py --data_paths=./data/user
        echo "USERRRRR"
      fi
      if [ $OPTARG == "son" ]
      then
        python tacotron2_train.py --data_paths=./data/son
        echo "SONNNNNN"
      fi
      ;;
  esac
done

# python tacotron2_train.py --data_path=./data/user

date

conda deactivate

squeue --job $SLURM_JOBID

echo "##### END #####"
