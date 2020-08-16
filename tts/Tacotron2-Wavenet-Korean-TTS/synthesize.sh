#!/bin/sh

#SBATCH -J KTacoSyn
#SBATCH -o KTacoSyn.%j.out
#SBATCH -p gpu-2080ti-8
#SBATCH -t 2:00:00
#SBATCH --gres=gpu:2

echo "Start Synthesizing Wav File"
echo "SLURM_SUBMIT_DIR = $SLURM_SUBMIT_DIR"
echo "CUDA_HOME = $CUDA_HOME"
echo "CUDA_VISIBLE_DEVICES = $CUDA_VISIBLE_DEVICES"
echo "CUDA_VERSION=$CUDA_VERSION"

srun -l /bin/hostname
srun -l /bin/pwd
srun -l /bin/date

conda init bash
conda activate tf1-gpu-py36

python synthesizer.py --load_path logs_tacotron2/son_2020-08-14_14-48-04 --num_speakers 1 --speaker_id 0 --text "안녕하세요 채승현입니다"

date

conda deactivate

squeue --job $SLURM_JOBID

echo "##### END #####"
