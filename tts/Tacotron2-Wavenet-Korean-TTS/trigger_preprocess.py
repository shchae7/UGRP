import os

# trigger preprocessing!
os.system('python preprocess.py --num_workers 8 --name user --in_dir ./datasets/user --out_dir ./data/user')
