is_palindrome <- function(num) {
    original <- num
    reversed_num <- 0
    while (num > 0) {
        reversed_num <- reversed_num * 10 + num %% 10
        num <- num %/% 10
    }
    return(original == reversed_num)
}

squared_sum <- function(N) {
    max_square <- floor(sqrt(N)) + 1
    sums <- rep(FALSE, N + 1)

    for (n in 1:max_square) {
        s <- 0
        for (m in n:max_square) {
            s <- s + m * m
            if (s > N) {
                break
            }
            if (m > n) {
                sums[s] <- TRUE
            }
        }
    }
    return(sums)
}

P125 <- function(N) {
    sums <- squared_sum(N)
    palindrome_sums <- rep(FALSE, N + 1)

    total <- 0
    for (i in 1:N) {
        if (sums[i] && is_palindrome(i) && !palindrome_sums[i]) {
            total <- total + i
            palindrome_sums[i] <- TRUE
        }
    }
    return(total)
}

cat(P125(100000000), "\n")
