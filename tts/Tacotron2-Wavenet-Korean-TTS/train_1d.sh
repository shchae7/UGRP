#!/bin/sh

#SBATCH -J KTacoTr
#SBATCH -o KTacoTr.%j.out
#SBATCH -p gpu-all
#SBATCH -t 1-00:00:00
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

python train_tacotron2.py

date

conda deactivate

squeue --job $SLURM_JOBID

echo "##### END #####"
