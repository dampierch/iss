# In-silico Consultation Report
A loose set of bash scripts with some R code to create an in-silico
consultation report using Latex.

## Usage
On biowulf via sinteractive or sbatch.

### sinteractive

```
./report.sh
path to input files (e.g. /data/dir/): /data/mydir/
```

- input files: `*_KNN.combined.csv` and `bin_classifier_output.csv`
- remember to include trailing `/` in path to these files

### sbatch

```
sbatch run.sh /path/to/input/files/
```

- input files: `*_KNN.combined.csv` and `bin_classifier_output.csv`
- remember to include trailing `/` in path to these files
- call `run.sh` from directory in which `run.sh` and `report.sh` are stored

## Expected behavior

The scripts should read `*_KNN.combined.csv` and `bin_classifier_output.csv`.

The scripts should return `*_iss_consult_report.pdf` in the same directory from
which the scripts are run, which must be the directory in which the scripts
and icon are stored.

The __Note__ section sometimes requires manual entry, but the goal is for
automation. See `note.tex`.

The Methods, Disclaimer, and References are static and fill automatically.
