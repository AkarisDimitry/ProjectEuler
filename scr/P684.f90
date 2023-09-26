! Modulo for calculations
INTEGER, PARAMETER :: MOD = 1000000007

! Propiedad de Exponenciación:
! Para la exponenciación modular, donde queremos calcular a^b \mod ma 
! b
!  modm, utilizamos un algoritmo eficiente que explota las propiedades del operador módulo.
! 
! La exponenciación modular se basa en las siguientes observaciones:
! 
! (a \cdot b) \mod m = ((a \mod m) \cdot (b \mod m)) \mod m(a⋅b)modm=((amodm)⋅(bmodm))modm
! (a \cdot b) \cdot c \mod m = ((a \mod m) \cdot (b \mod m) \cdot (c \mod m)) \mod m(a⋅b)⋅cmodm=((amodm)⋅(bmodm)⋅(cmodm))modm
! Entonces, para calcular a^b \mod ma 
! b
!  modm, el algoritmo es algo como esto (usando una versión de la exponenciación binaria):
! 
! Inicializar un resultado a 11.
! Mientras b > 0b>0:
! Si bb es impar, entonces multiplicar el resultado por aa y tomar \mod mmodm.
! Dividir bb por 22 (o realizar un desplazamiento hacia la derecha si estamos trabajando en nivel de bits).
! Elevar aa al cuadrado y tomar \mod mmodm.
! El resultado final es a^b \mod ma 
! b
!  modm.
! Así, el algoritmo utiliza la propiedad de que puedes tomar el módulo en cada paso del cálculo sin afectar el resultado final.

! A function to calculate the power of a number modulo MOD
! Time Complexity: O(log(exp))
! Space Complexity: O(1)
RECURSIVE FUNCTION power(base, exp) RESULT(res)
  INTEGER, INTENT(IN) :: base, exp
  INTEGER :: res
  IF (exp == 0) THEN
    res = 1
  ELSE IF (MOD(exp, 2) == 1) THEN
    res = MOD(base * power(base, exp - 1), MOD) ! Multiply the result by base if exp is odd
  ELSE
    res = power(base * base, exp / 2) ! Square the base and divide the exponent by 2
  END IF
END FUNCTION power

! A function to compute S(k) in a non-modular space
! Time Complexity: O(log(k))
! Space Complexity: O(1)
FUNCTION S(k) RESULT(res)
  INTEGER, INTENT(IN) :: k
  INTEGER :: res, n, r
  n = k / 9
  r = MOD(k, 9) + 2
  res = (((r - 1) * r + 10) * power(10, n) - 2 * (r + 9 * n + 4)) / 2
END FUNCTION S

! A function to compute S(k) in a modular space
! Time Complexity: O(log(k))
! Space Complexity: O(1)
FUNCTION modular_S(k) RESULT(res)
  INTEGER, INTENT(IN) :: k
  INTEGER :: res, n, r
  n = k / 9
  r = MOD(k, 9) + 2
  res = MOD((((r - 1) * r + 10) * power(10, n) - 2 * (r + 9 * n + 4)) * power(2, MOD - 2), MOD)
END FUNCTION modular_S

! A function to generate Fibonacci numbers up to n
! Time Complexity: O(n)
! Space Complexity: O(n)
SUBROUTINE fib(n, fib_numbers)
  INTEGER, INTENT(IN) :: n
  INTEGER, DIMENSION(n) :: fib_numbers
  INTEGER :: a, b, temp, i
  a = 0
  b = 1
  DO i = 1, n
    fib_numbers(i) = a
    temp = a
    a = b
    b = temp + b
  END DO
END SUBROUTINE fib

! The main program to compute the result
! Time Complexity: O(n*log(k)) where n is the number of Fibonacci numbers and k is the Fibonacci number
! Space Complexity: O(n)
PROGRAM main
  INTEGER :: n, result, i
  INTEGER, DIMENSION(91) :: fib_numbers
  ! Testing the functions
  IF (S(20) /= 1074 .OR. S(49) /= 1999945 .OR. modular_S(20) /= 1074 .OR. modular_S(49) /= 1999945) THEN
    PRINT *, "Function tests failed!"
    STOP
  END IF
  ! Calculating the result
  n = 91
  CALL fib(n, fib_numbers)
  result = 0
  DO i = 3, n
    result = MOD(result + modular_S(fib_numbers(i)), MOD)
  END DO
  PRINT *, "Result: ", result
END PROGRAM main
