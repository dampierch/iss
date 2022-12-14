#!/bin/bash

## bash script to create consultation report
## usage on biowulf via sinteractive or sbatch
## ex1: ./report (will request input path)
## ex2: sbatch run.sh /path/to/input/files/ 

export TMP=tmp/
path=$1

prepare_input() {
    printf "preparing input...\n"

    l=${#path}
    if [ "${l}" -gt 0 ]
    then
        indir=${path}
    else
        printf "path to input files (e.g. /data/dir/): "
        read indir
    fi

    mkdir -p ${TMP}
    rsync -avz ${indir}*_KNN.combined.csv ${TMP}
    rsync -avz ${indir}bin_classifier_output.csv ${TMP}

    dos2unix ${TMP}*.csv
}

run_r() {
    printf "running R...\n"
    nci_fields="Consistency_class Consistency_score"
    dkfz_fields="ID Sample Class1 Class1.score CNSv12b6.subclass1 CNSv12b6.subclass1.score"
    module load R
    Rscript make_tex.r --args ${nci_fields} ${dkfz_fields}
}

make_tex() {
    printf "making latex document...\n"
    tname=iss_consult_report
    sid=$(<tmp/sample.tex)
    rname=${sid}_${tname}
    module load tex
    pdflatex ${tname}
    pdflatex ${tname} && mv ${tname}.pdf ${rname}.pdf
    if [ -f ${rname}.pdf ]
    then
        printf "%s.pdf exists!\nremoving intermediate files...\n" "${rname}"
        for e in aux bcf log out run.xml
        do
            rm ${tname}.${e}
        done
        printf "cleaning up input...\n"
        rm -r ${TMP}
    else
        printf "%s.pdf does not exist\nrecommend investigation...\n" "${rname}"
    fi
}

prepare_input
run_r
make_tex
