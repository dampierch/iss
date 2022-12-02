#!/bin/bash

## bash script to create consultation report

export TMP=tmp/

prepare_input() {
    printf "preparing input...\n"
    printf "path to input files (e.g. /data/dir/): "
    read indir

    mkdir -p ${TMP}
    rsync -avz ${indir}*_KNN.combined.csv ${TMP}
    rsync -avz ${indir}bin_classifier_output.csv ${TMP}

    dos2unix ${TMP}*.csv
}

run_r() {
    printf "running R...\n"
    module load R
    Rscript make_tex.r
}

make_tex() {
    printf "making latex document...\n"
    module load tex
    fpre=iss_consult_report
    pdflatex ${fpre}
    pdflatex ${fpre}
    if [ -f ${fpre}.pdf ]
    then
        printf "%s.pdf exists!\nremoving intermediate files...\n" "${fpre}"
        for e in aux bcf log out run.xml
        do
            rm ${fpre}.${e}
        done
    else
        printf "%s.pdf does not exist\nrecommend investigation...\n" "${fpre}"
    fi
}

cleanup_input() {
    if [ -f *.pdf ]
    then
        printf "cleaning up input...\n"
        rm -r ${TMP}
    fi
}

prepare_input
run_r
make_tex
cleanup_input
