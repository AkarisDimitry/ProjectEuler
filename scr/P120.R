# Calculate the maximum remainder for a given 'a'
maxRemainder <- function(a) {
  remainders <- numeric(0)  # Vector to store remainders
  max_r <- 0
  n <- 1
  
  while(TRUE) {
    r <- ((a - 1)^n + (a + 1)^n) %% (a^2)
    
    # Check if the remainder is already found
    if (r %in% remainders) {
      break  # Break if the remainder starts repeating
    }
    
    remainders <- c(remainders, r)
    max_r <- max(max_r, r)
    
    n <- n + 2  # Increment by 2 as even 'n' does not produce max remainder
  }
  
  return(max_r)
}

# Main function to calculate the sum of maximum remainders for each 'a' in the range 3 to N
P120 <- function(N) {
  sum(sapply(3:N, maxRemainder))
}

# Measure execution time and call P120
start_time <- Sys.time()
result <- P120(1000)
end_time <- Sys.time()

# Output
cat("Result of P120:", result, "\n")
cat("Execution time:", end_time - start_time, "seconds\n")
