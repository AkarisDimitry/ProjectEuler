# Function to calculate the probability distribution of dice rolls
calculateProbabilityDistribution <- function(numDice, sides) {
  outcomes <- expand.grid(replicate(numDice, 1:sides, simplify = FALSE))
  sums <- rowSums(outcomes)
  frequency <- table(sums)
  probabilityDistribution <- frequency / length(sums)
  return(probabilityDistribution)
}

# Calculate probability distribution for Peter (9 four-sided dice)
peterDistribution <- calculateProbabilityDistribution(9, 4)

# Calculate probability distribution for Colin (6 six-sided dice)
colinDistribution <- calculateProbabilityDistribution(6, 6)

# Function to calculate the probability that Peter's sum is greater than Colin's
peterBeatsColinProbability <- function(peterDistribution, colinDistribution) {
  probability <- 0
  for (peterSum in names(peterDistribution)) {
    colinProbSum <- sum(colinDistribution[names(colinDistribution) < peterSum])
    probability <- probability + peterDistribution[peterSum] * colinProbSum
  }
  return(probability)
}

# Measure execution time
start.time <- Sys.time()
result <- peterBeatsColinProbability(peterDistribution, colinDistribution)
end.time <- Sys.time()
execution.time <- end.time - start.time

# Output
cat("Probability that Pyramidal Peter beats Cubic Colin:", round(result, 7), "\n")
cat("Execution time:", execution.time, "seconds\n")
