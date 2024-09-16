#!/bin/bash
#SBATCH --cpus-per-task=18
#SBATCH --partition=2080-galvani
#SBATCH --nodes=1
#SBATCH --mem=40G
#SBATCH --time=3-00:00:00
#SBATCH -o /mnt/qb/akata/jstrueber72/logs/tar_job_%j.out
#SBATCH -e /mnt/qb/akata/jstrueber72/logs/tar_job_%j.err

# Ensure pigz is available in the PATH
module load pigz

# Use tar with pigz for parallel compression
tar --use-compress-program=pigz -cf toys200.tar.gz toys200/