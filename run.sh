#!/bin/bash

## bash code to run report.sh, which requires backend for R

#SBATCH --partition=norm
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --ntasks-per-core=1
#SBATCH --mem=1g
#SBATCH --requeue
#SBATCH --time=00:05:00
#SBATCH --mail-type=END
#SBATCH --mail-user=chris.dampier@nih.gov

./report.sh