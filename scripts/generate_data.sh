#!/bin/bash
#SBATCH --cpus-per-task=8
#SBATCH --partition=2080-galvani
#SBATCH --gres=gpu:1
#SBATCH --nodes=1
#SBATCH --mem=30G
#SBATCH --time=1-00:00:00
#SBATCH -o /mnt/qb/akata/jstrueber72/logs/toys200_job_%j.out
#SBATCH -e /mnt/qb/akata/jstrueber72/logs/toys200_job_%j.err

python generate_data_pose_list.py -start=0 -end=200
