#!/bin/sh

#SBATCH -J KTacoTr
#SBATCH -o KTacoTr.%j.out
#SBATCH -p gpu-titanxp
#SBATCH -t 36:00:00
#SBATCH --gres=gpu:1

echo "Start Training Korean Tacotron2"
echo "SLURM_SUBMIT_DIR = $SLURM_SUBMIT_DIR"
echo "CUDA_HOME = $CUDA_HOME"
echo "CUDA_VISIBLE_DEVICES = $CUDA_VISIBLE_DEVICES"
echo "CUDA_VERSION=$CUDA_VERSION"

srun -l /bin/hostname
srun -l /bin/pwd
srun -l /bin/date

python train_vocoder.py

date

squeue --job $SLURM_JOBID

echo "##### END #####"
