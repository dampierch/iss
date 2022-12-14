library(readr)

format_x <- function(x) {
    if (is.numeric(x)) {
        x <- format(round(x, 3), nsmall=3)
    } else {
        if (grepl(": ", x)) {
            x <- unlist(strsplit(x, " :"))[1]
        }
    }
    return(x)
}

make_tex <- function(df, l) {
    ## for bin_classifier_output.csv key fields are
    ##     c("Consistency_class", "Consistency_score")
    ## for *_KNN_combined.csv key fields are
    ##     c("ID", "Sample", "Class1", "Class1.score", "CNSv12b6.subclass1",
    ##        "CNSv12b6.subclass1.score")
    if (l$nci_fields[1] %in% colnames(df)) {
        j <- l$nci_fields
    } else {
        j <- l$dkfz_fields
    }
    for (e in j) {
        f <- paste0(Sys.getenv("TMP"), tolower(e), ".tex")
        x <- unname(unlist(df[1, e]))
        x <- format_x(x)
        l[[e]] <- x
        if (grepl("_", x)) {
            cat(unlist(strsplit(x, "_")), sep="\\_", file=f)
        } else {
            write(x, file=f)
        }
    }
    return(l)
}

make_diagnosis <- function(l, threshold=0.85) {
    ## take results from classifiers as elements of list and perform logic
    ## if all classifiers give same result with high score, diagnosis is made
    ## otherwise, diagnosis is uncertain
    c1 <- l[[l$nci_fields[1]]] == l[[l$dkfz_fields[3]]]
    c2 <- l[[l$nci_fields[1]]] == l[[l$dkfz_fields[5]]]
    c3 <- as.numeric(l[[l$nci_fields[2]]]) >= threshold
    c4 <- as.numeric(l[[l$dkfz_fields[4]]]) >= threshold
    c5 <- as.numeric(l[[l$dkfz_fields[6]]]) >= threshold
    if (c1 & c2 & c3 & c4 & c5) {
        f <- paste0(Sys.getenv("TMP"), "cc", ".tex")
        write(l[[l$nci_fields[1]]], file=f)
        f <- paste0(Sys.getenv("TMP"), "diagnosis", ".tex")
        write(l[[l$nci_fields[1]]], file=f)
        f <- paste0(Sys.getenv("TMP"), "score_type", ".tex")
        write("high-score", file=f)
    } else {
        f <- paste0(Sys.getenv("TMP"), "cc", ".tex")
        write("See note", file=f)
        f <- paste0(Sys.getenv("TMP"), "diagnosis", ".tex")
        write(l[[l$nci_fields[1]]], file=f)
        f <- paste0(Sys.getenv("TMP"), "score_type", ".tex")
        write("possible", file=f)        
    }
}

main <- function() {
    ## args reads "--args" even with trailingOnly set to TRUE
    args <- commandArgs(trailingOnly=TRUE)
    l <- list(nci_fields=args[2:3], dkfz_fields=args[4:9])
    f <- paste0(Sys.getenv("TMP"), "bin_classifier_output.csv")
    df <- read_csv(f)
    l <- make_tex(df, l)
    f <- Sys.glob(paste0(Sys.getenv("TMP"), "*_KNN.combined.csv"))
    df <- read_csv(f)
    l <- make_tex(df, l)
    make_diagnosis(l)
}

main()
