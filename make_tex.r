library(readr)

format_x <- function(x) {
    if (is.numeric(x)) {
        x <- format(round(x, 3), nsmall=3)
    } else {
        if (grepl(": ", x)) {
            x <- unlist(strsplit(x, ": "))[2]
        }
    }
    return(x)
}

make_tex <- function(df) {
    if ("Consistency_class" %in% colnames(df)) {
        j <- c("Consistency_class", "Consistency_score")
    } else {
        j <- c(
            "ID", "Sample", "Class1", "Class1.score", "CNSv12b6.subclass1",
            "CNSv12b6.subclass1.score"
        )
    }
    for (e in j) {
        f <- paste0("input/", tolower(e), ".tex")
        x <- unname(unlist(df[1, e]))
        x <- format_x(x)
        if (grepl("_", x)) {
            cat(unlist(strsplit(x, "_")), sep="\\_", file=f)
        } else {
            write(x, file=f)
        }
    }
}

main <- function() {
    df <- read_csv("input/bin_classifier_output.csv")
    make_tex(df)
    df <- read_csv("input/206648960113_KNN.combined.csv")
    make_tex(df)
}

main()
