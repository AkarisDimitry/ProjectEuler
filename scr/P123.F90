PROGRAM Main
    IMPLICIT NONE
    INTEGER, PARAMETER :: upper_bound = 10000  ! Estimated upper bound for the sieve.
    INTEGER, PARAMETER :: threshold = 10000000000  ! 10^10
    LOGICAL, ALLOCATABLE :: primes(:)
    INTEGER :: idx

    ! Generate prime numbers using the Sieve of Eratosthenes.
    primes = sieve_of_eratosthenes(upper_bound)

    ! Find the least value of n for which the remainder first exceeds 10^10.
    DO idx = 2, upper_bound
        IF (primes(idx)) THEN
            IF (2 + 2 * idx > threshold) EXIT
        END IF
    END DO

    PRINT *, "The result is: ", idx
CONTAINS
    FUNCTION sieve_of_eratosthenes(limit) RESULT(sieve)
        INTEGER, INTENT(IN) :: limit
        LOGICAL, ALLOCATABLE :: sieve(:)
        INTEGER :: i, j

        ALLOCATE(sieve(0:limit))
        sieve = .TRUE.
        sieve(0) = .FALSE.
        sieve(1) = .FALSE.
        
        ! Eliminate the non-primes.
        DO i = 2, SQRT(REAL(limit))
            IF (sieve(i)) THEN
                DO j = i * i, limit, i
                    sieve(j) = .FALSE.
                END DO
            END IF
        END DO
    END FUNCTION sieve_of_eratosthenes
END PROGRAM Main

/*
    '''
    <p>Let $p_n$ be the $n$th prime: $2, 3, 5, 7, 11, dots$, and let $r$ be the 
    remainder when $(p_n - 1)^n + (p_n + 1)^n$ is divided by $p_n^2$.</p>
    <p>For example, when $n = 3$, $p_3 = 5$, and $4^3 + 6^3 = 280 equiv 5 mod 25$.</p>
    <p>The least value of $n$ for which the remainder first exceeds $10^9$ is $7037$.</p>
    <p>Find the least value of $n$ for which the remainder first exceeds $10^{10}$.</p>
    ''' 

    '''
    This problem is interesting in that it deals with modular arithmetic and prime numbers. Let's break it down step by step.

    Given:
    \[
    (p_n - 1)^n + (p_n + 1)^n \equiv r \pmod{p_n^2}
    \]

    We want to find the smallest \( n \) such that \( r > 10^{10} \).

    Notice that \( (p_n - 1)^n \) will always be \( -1 \) mod \( p_n \)
     because \( (p_n - 1) \) is \( -1 \) mod \( p_n \) and raising \( -1 \)
      to an odd power will always be \( -1 \) while raising it to an even 
      power will be \( 1 \). Since \( p_n \) is always odd except for 
      \( p_1 \), \( n \) will always be \( -1 \) or \( 1 \) mod \( p_n \).

    Similarly, \( (p_n + 1)^n \) will always be \( 1 \) mod \( p_n \).

    Thus:
    \[
    (p_n - 1)^n + (p_n + 1)^n \equiv -1^n + 1^n \pmod{p_n}
    \]

    This is either \( 0 \) or \( 2 \) mod \( p_n \). Notice that if it's 
    \( 0 \) mod \( p_n \), then it's also \( 0 \) mod \( p_n^2 \). So, we
     only need to consider the cases where it's \( 2 \) mod \( p_n \).

    For those cases, we know:
    \[
    (p_n - 1)^n + (p_n + 1)^n \equiv 2 \pmod{p_n}
    \]

    We want to find out what this is mod \( p_n^2 \).

    The value of \( (p_n - 1)^n + (p_n + 1)^n \) can be expanded using 
    the binomial theorem:

    \[
    (p_n - 1)^n = \sum_{k=0}^{n} (-1)^k \binom{n}{k} p_n^{n-k}
    \]
    \[
    (p_n + 1)^n = \sum_{k=0}^{n} \binom{n}{k} p_n^{n-k}
    \]

    Now, for terms where \( k \) is at least 2, \( p_n^{n-k} \) will be 
    \( 0 \) mod \( p_n^2 \) because it will have at least \( p_n^2 \) as 
    a factor. So, we only need to consider the first two terms for each:

    \[
    (p_n - 1)^n \equiv (-1 + np_n) \pmod{p_n^2}
    \]
    \[
    (p_n + 1)^n \equiv (1 + np_n) \pmod{p_n^2}
    \]

    Combining, we get:

    \[
    (p_n - 1)^n + (p_n + 1)^n \equiv 2 + 2np_n \pmod{p_n^2}
    \]

    Since we're looking for the first \( n \) where this exceeds \( 10^{10}
     \), we can set up the inequality:

    \[
    2 + 2np_n > 10^{10}
    \]

    Now, we can iterate through values of \( n \), compute \( p_n \) 
    (the \( n \)-th prime), and check the above inequality to find the 
    least \( n \) for which the remainder first exceeds \( 10^{10} \).
*/