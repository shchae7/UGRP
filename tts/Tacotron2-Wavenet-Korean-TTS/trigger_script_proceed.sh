srun -l /bin/hostname
srun -l /bin/pwd
srun -l /bin/date

#make user directory
rm -rf datasets/user/audio
mkdir datasets/user/audio
#preprocess
conda init bash
source activate tf1-demo-env

python trigger_preprocess.py & sh datasets/user/mv_wav.sh

date

conda deactivate

#wait for preprocessing
sleep 15 #15s

#start to train taco2 with user's data
python trigger_taco2_train.py

#start to train wavenet with user's data
python trigger_wave_train.py

echo "##### END #####"