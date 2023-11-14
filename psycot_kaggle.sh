#!/bin/bash
#SBATCH --output=output_report-%j.out
#SBATCH --job-name=llama2
#SBATCH --gres=gpu:A6000:4
# SBATCH --partition=long-inst
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=60G
#SBATCH --time=1-6:00:00
#SBATCH --mail-type=end
#SBATCH --mail-user=zw3@cs.cmu.edu

source ~/.bashrc
conda activate psycot
cd ~/Assignment-3-ANLP
python3 psycot_kaggle.py