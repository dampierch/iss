#!/bin/bash

## bash script to create consultation report

OUTDIR=input/

prepare_input() {
    printf "preparing input...\n"
    indir=/data/MDATA/compass/external_raw/206648960113/

    mkdir -p ${OUTDIR}
    rsync -avz ${indir}*_KNN.combined.csv ${OUTDIR}
    rsync -avz ${indir}bin_classifier_output.csv ${OUTDIR}

    dos2unix ${OUTDIR}*.csv
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
        rm -r ${OUTDIR}
    fi
}

prepare_input
run_r
make_tex
cleanup_input
