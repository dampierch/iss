# In-silico Consultation Report
A loose set of bash scripts with some R code to create an in-silico
consultation report using Latex.

## Usage
On biowulf via sinteractive or sbatch

### sinteractive

```
./report
path to input files (e.g. /data/dir/): /data/mydir/
```

- remember to include trailing `/` in path

### sbatch

```
run.sh /path/to/input/files/
```

- remember to include trailing `/` in path

## Expected behaviod

The scripts should read `*_KNN.combined.csv` and `bin_classifier_output.csv`.

The scripts should return `iss_consult_report.pdf` in the same directory from
which the scripts are run, which must be the directory in which the scripts
and icon are stored.

The _Note_ section requires manual entry at the moment but will eventually be
automated. See `note.tex`.

The Methods, Disclaimer, and References are static and fill automatically.
