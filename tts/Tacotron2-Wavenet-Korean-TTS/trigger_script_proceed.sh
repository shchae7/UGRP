srun -l /bin/hostname
srun -l /bin/pwd
srun -l /bin/date

#some directory settings
rm -rf datasets/user/audio
rm -rf ../../script/server/script_line/end_of_training.txt
mkdir datasets/user/audio
#preprocess
conda init bash
source activate tf1-demo-env

#python trigger_preprocess.py & sh datasets/user/mv_wav.sh
python trigger_preprocess.py
date
conda deactivate

#wait for preprocessing
sleep 15 #15s

#start to train taco2 with user's data
python trigger_taco2_train.py

#start to train wavenet with user's data
python trigger_wave_train.py

#alert its end
sleep 15 #15s
echo 'Hello, world.' >../../script/server/script_line/end_of_training.txt

echo "##### END #####"