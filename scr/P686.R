pe686 <- function(target) {
  upper_limit <- log10(1.24)
  lower_limit <- log10(1.23)
  n <- log10(2^196)
  m <- log10(2^93)
  x <- log10(2^12710)
  i <- 12710
  nth <- 45

  while (nth < target) {
    x <- x + n
    i <- i + 196
    d <- x - floor(x)

    if (d > lower_limit && d < upper_limit) {
      nth <- nth + 1
      next
    }

    x <- x + m
    i <- i + 93
    d <- x - floor(x)

    if (d > lower_limit && d < upper_limit) {
      nth <- nth + 1
    }
  }

  return(i)
}

# Measure execution time and run the function
start_time <- Sys.time()
result <- pe686(678910)
end_time <- Sys.time()

elapsed_time <- end_time - start_time
cat("pe686 took", elapsed_time, "seconds to run.\n")
cat("Output:", result, "\n")
