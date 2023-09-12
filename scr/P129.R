# A number consisting entirely of ones is called a repunit. We shall
# define R(k) to be a repunit of length k; for example, R(6) = 111111.
# Given that n is a positive integer and gcd(n, 10) = 1, it can 
# be shown that there always exists a value, k, for which R(k) is 
# divisible by n, and let A(n) be the least such value of k; for 
# example, A(7) = 6 and A(41) = 5.
# The least value of n for which A(n) first exceeds ten is 17.
# Find the least value of n for which A(n) first exceeds one-million.

P129b <- function(N) {
  k_max <- 0 # Initializing the maximum value of k
  for (n in (N/10-1000):(N-1)) {
    # Ensuring the number isn't divisible by 2 or 5
    if (n %% 2 != 0 && n %% 5 != 0) {
      k <- 2 # Initializing the value of k
      res <- 11 # Initializing the residual value
      res0 <- 10 # Another residual value

      while (res != 0) {
        # Updating the value of res0
        res0 <- (res0 * 10) %% n
        # Updating the value of res
        res <- (res0 + res) %% n
        k <- k + 1 # Incrementing the value of k
      }

      # Updating the maximum value of k if the current k is greater
      if (k > k_max) {
        k_max <- k
      }
      if (k > 1e6) {
        break
      }
    }
  }
  return(k_max) # Returning the maximum value of k
}

# Measuring execution time and printing the result
start_time <- Sys.time()
result <- P129b(1e7)
end_time <- Sys.time()
cat("Result of P129b :", result, "(execution time", end_time - start_time, "seconds)\n")
