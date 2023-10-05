PROGRAM P710_program
  IMPLICIT NONE

  INTEGER, PARAMETER :: MOD = 1000000
  INTEGER :: n, result
  INTEGER(KIND=8) :: palOdd, palOdd0b2, palOdd0b4
  INTEGER(KIND=8) :: twoPalOdd, twoPalOdd0b2, twoPalOdd0b4
  INTEGER(KIND=8) :: twoPal, sumaOdd, sumaEven

  ! Inicialización de variables
  palOdd = 0
  palOdd0b2 = 2
  palOdd0b4 = 1
  twoPalOdd = 0
  twoPalOdd0b2 = 1
  twoPalOdd0b4 = 0
  twoPal = 0
  sumaOdd = 0
  sumaEven = 0
  n = 2

  ! Ejecuta la función P710
  result = P710(n, palOdd, palOdd0b2, palOdd0b4, twoPalOdd, twoPalOdd0b2, twoPalOdd0b4, twoPal, sumaOdd, sumaEven)

  ! Imprime el resultado
  PRINT *, "Result of P710: ", result

CONTAINS

  ! Función para calcular potencia con módulo
  INTEGER(KIND=8) FUNCTION powMod(base, exponent, mod)
    INTEGER(KIND=8), INTENT(IN) :: base, exponent, mod
    INTEGER(KIND=8) :: result

    result = 1_8
    base = MODULO(base, mod)

    DO WHILE (exponent > 0)
      IF (MODULO(exponent, 2) == 1) THEN
        result = MODULO(result * base, mod)
      END IF
      base = MODULO(base * base, mod)
      exponent = exponent / 2
    END DO

    powMod = MODULO(result, mod)
  END FUNCTION powMod

  ! Función principal para calcular el valor deseado
  INTEGER FUNCTION P710(n, palOdd, palOdd0b2, palOdd0b4, twoPalOdd, twoPalOdd0b2, twoPalOdd0b4, twoPal, sumaOdd, sumaEven)
    INTEGER, INTENT(INOUT) :: n
    INTEGER(KIND=8), INTENT(INOUT) :: palOdd, palOdd0b2, palOdd0b4, twoPalOdd, twoPalOdd0b2, twoPalOdd0b4, twoPal, sumaOdd, sumaEven

    DO WHILE (twoPal /= MOD .OR. n < 42)
      n = n + 2
      palOdd = powMod(2, n/2 - 1, MOD)
      twoPalOdd = MODULO(sumaOdd - twoPalOdd0b4 + palOdd0b4, MOD)
      twoPal = MODULO(twoPalOdd + sumaEven - twoPalOdd0b2 + palOdd0b2, MOD)
      sumaOdd = sumaOdd + twoPalOdd
      sumaEven = sumaEven + twoPalOdd
      palOdd0b4 = palOdd0b2
      palOdd0b2 = palOdd
      twoPalOdd0b4 = twoPalOdd0b2
      twoPalOdd0b2 = twoPalOdd
    END DO

    P710 = n
  END FUNCTION P710

END PROGRAM P710_program
