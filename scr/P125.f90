PROGRAM P125
    IMPLICIT NONE
    INTEGER, PARAMETER :: N = 100000000
    INTEGER :: i
    LOGICAL, ALLOCATABLE :: sums(:), palindrome_sums(:)
    INTEGER(KIND=8) :: total

    ALLOCATE(sums(0:N))
    ALLOCATE(palindrome_sums(0:N))
    sums = .FALSE.
    palindrome_sums = .FALSE.

    CALL squared_sum(N, sums)

    total = 0
    DO i = 0, N
        IF (sums(i) .AND. is_palindrome(i) .AND. .NOT. palindrome_sums(i)) THEN
            total = total + i
            palindrome_sums(i) = .TRUE.
        END IF
    END DO

    PRINT *, total

CONTAINS

    FUNCTION is_palindrome(num) RESULT(is_pal)
        INTEGER, INTENT(IN) :: num
        INTEGER :: original, reversed_num, remainder
        LOGICAL :: is_pal

        original = num
        reversed_num = 0
        DO
            IF (num == 0) EXIT
            remainder = MOD(num, 10)
            reversed_num = reversed_num * 10 + remainder
            num = num / 10
        END DO

        is_pal = (original == reversed_num)
    END FUNCTION is_palindrome

    SUBROUTINE squared_sum(N, sums)
        INTEGER, INTENT(IN) :: N
        LOGICAL, INTENT(OUT) :: sums(0:N)
        INTEGER :: n, m, max_square
        INTEGER(KIND=8) :: s

        max_square = NINT(SQRT(REAL(N))) + 1
        sums = .FALSE.

        DO n = 1, max_square
            s = 0
            DO m = n, max_square
                s = s + m * m
                IF (s > N) EXIT
                IF (m > n) sums(s) = .TRUE.
            END DO
        END DO
    END SUBROUTINE squared_sum

END PROGRAM P125
