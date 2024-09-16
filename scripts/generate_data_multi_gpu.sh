#!/bin/bash
#SBATCH --cpus-per-task=8
#SBATCH --partition=2080-galvani
#SBATCH --gres=gpu:1
#SBATCH --nodes=1
#SBATCH --mem=40G
#SBATCH --time=1-00:00:00
#SBATCH --array=0-14
#SBATCH -o /mnt/qb/akata/jstrueber72/logs/toys200_job_%A_%a.out
#SBATCH -e /mnt/qb/akata/jstrueber72/logs/toys200_job_%A_%a.err

# Calculate start and end based on SLURM_ARRAY_TASK_ID
start=${10 * SLURM_ARRAY_TASK_ID + 62}
end=${(10 * (SLURM_ARRAY_TASK_ID + 1) + 62)}

python generate_data_pose_list.py -start=${start} -end=${end}