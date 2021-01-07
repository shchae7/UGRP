#!/bin/sh

#SBATCH -J KWaveTr
#SBATCH -o ./out_files/KWaveTr.%j.out
#SBATCH -p titanxp
#SBATCH -t 02:00:00
#SBATCH --gres=gpu:2

echo "Start Training Korean Wavenet Vocoder"
echo "SLURM_SUBMIT_DIR = $SLURM_SUBMIT_DIR"
echo "CUDA_HOME = $CUDA_HOME"
echo "CUDA_VISIBLE_DEVICES = $CUDA_VISIBLE_DEVICES"
echo "CUDA_VERSION=$CUDA_VERSION"

srun -l /bin/hostname
srun -l /bin/pwd
srun -l /bin/date

conda init bash
conda activate tf2-gpu-py36

while getopts "u:" opt; do
  case $opt in
    u)
      echo >&2 "-u was triggered!, OPTARG: $OPTARG"
      if [ $OPTARG == "user" ]
      then
        python vocoder_train.py --data_dir=./data/user
        echo "USERRRRR"
      fi
      if [ $OPTARG == "son" ]
      then
        python vocoder_train.py --data_dir=./data/son
        echo "SONNNNNN"
      fi
      ;;
  esac
done

#python vocoder_train.py

date

conda deactivate

squeue --job $SLURM_JOBID

echo "##### END #####"
