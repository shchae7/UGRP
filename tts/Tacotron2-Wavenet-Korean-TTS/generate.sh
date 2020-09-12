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


#python generate.py --load_path logs_tacotron2/son_2020-08-14_14-48-04 --num_speakers 1 --speaker_id 0 --text "안녕하세요 채승현입니다"
#python generate.py --mel ./logs_tacotron2/generate/2020-08-30-19-16-06.npy --gc_cardinality 2 --gc_id 0 ./logdir-wavenet/train/2020-08-26T00-06-25
python generate.py --mel ./logs_tacotron2/generate/2020-08-30_19-16-06.npy --gc_cardinality 2 --gc_id 0 ./logs-tacotron2/train_sample
date


squeue --job $SLURM_JOBID

echo "##### END #####"
