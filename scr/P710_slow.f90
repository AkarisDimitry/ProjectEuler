PROGRAM P710_program
  IMPLICIT NONE

  INTEGER, PARAMETER :: N = 6, MOD = 1000000, SIZE = 1000000
  INTEGER :: result
  DOUBLE PRECISION :: start, finish, elapsed_time
  INTEGER, DIMENSION(SIZE) :: a, u

  ! Initialize arrays and variables
  a = 0
  u = 0
  u(3) = 1
  
  ! Get the starting time
  CALL CPU_TIME(start)

  ! Execute the P710 function
  result = P710(a, u)

  ! Get the ending time
  CALL CPU_TIME(finish)
  
  elapsed_time = finish - start

  ! Print the result and the elapsed time
  PRINT *, "Result of P710: ", result, " (execution time ", elapsed_time, " seconds)"

CONTAINS

  INTEGER FUNCTION P710(a, u)
    INTEGER, DIMENSION(:), INTENT(INOUT) :: a, u
    INTEGER :: n, v, w

    n = 3

    DO
      a(n+1) = MODULO((a(n) + a(n-1) + a(n-3)), MOD)
      a(n+2) = MODULO((a(n+1) + a(n) + a(n-2)), MOD)

      n = n + 2

      w = MODULO((u(n-2) + u(n-3)), MOD)
      v = MODULO((w + a((n-1)/2)), MOD)

      u(n) = v
      u(n+1) = w

      IF (w == 0 .OR. v == 0) EXIT
    END DO

    P710 = n - 1

  END FUNCTION P710

END PROGRAM P710_program
