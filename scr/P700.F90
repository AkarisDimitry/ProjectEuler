PROGRAM EulerCoins
    IMPLICIT NONE
    INTEGER(KIND=8) :: result  ! Declaración de la variable result con 8 bytes de tamaño

    result = compute()         ! Llama a la función compute y almacena el resultado en result
    PRINT *, result            ! Imprime el resultado
    STOP                      ! Termina el programa
END PROGRAM EulerCoins

! Función compute
! Esta función lleva a cabo la principal lógica para calcular la suma de Eulercoins.
! Complejidad temporal: O(n) para la búsqueda principal de Eulercoins.
! Complejidad espacial: O(n) para almacenar los Eulercoins.
INTEGER(KIND=8) FUNCTION compute()
    IMPLICIT NONE
    INTEGER(KIND=8), PARAMETER :: a = 1504170715041707_8  ! Declara e inicializa la constante a
    INTEGER(KIND=8), PARAMETER :: m = 4503599627370517_8  ! Declara e inicializa la constante m
    INTEGER(KIND=8) :: eulercoins(2000)                   ! Array para almacenar Eulercoins
    INTEGER :: coins_count = 1                            ! Contador para los Eulercoins encontrados
    INTEGER(KIND=8) :: currentEulercoin, inv, n, number, newCurrEulercoin, currMax

    eulercoins(1) = a            ! Inicializa el primer Eulercoin
    currentEulercoin = a         ! Establece el Eulercoin actual
    inv = powMod(a, m-2_8, m)    ! Calcula el inverso modular
    n = 2_8                      ! Establece el valor inicial de n

    ! Búsqueda principal para encontrar los Eulercoins
    DO
        number = MOD(a * n, m)   ! Calcula el siguiente posible Eulercoin
        IF (number < currentEulercoin) THEN
            currentEulercoin = number                   ! Actualiza el Eulercoin actual
            coins_count = coins_count + 1               ! Incrementa el contador
            eulercoins(coins_count) = number            ! Almacena el nuevo Eulercoin
        END IF

        ! Condición para cambiar de estrategia de búsqueda
        IF (currentEulercoin == 15806432_8) THEN
            newCurrEulercoin = 1_8         ! Establece el valor inicial para el nuevo Eulercoin
            currMax = m                     ! Establece el valor máximo actual

            ! Búsqueda de abajo hacia arriba para encontrar los Eulercoins
            DO WHILE (newCurrEulercoin /= 15806432_8)
                number = MOD(inv * newCurrEulercoin, m)
                IF (number < currMax) THEN
                    currMax = number
                    coins_count = coins_count + 1
                    eulercoins(coins_count) = newCurrEulercoin
                END IF
                newCurrEulercoin = newCurrEulercoin + 1_8
            END DO

            EXIT  ! Sale del bucle DO principal
        END IF

        n = n + 1_8  ! Incrementa el valor de n
    END DO

    compute = SUM(eulercoins(1:coins_count))  ! Calcula la suma total de los Eulercoins
    RETURN
END FUNCTION compute

! Función powMod
! Esta función calcula la exponenciación modular.
! Complejidad temporal: O(log(exp))
! Complejidad espacial: O(1)
INTEGER(KIND=8) FUNCTION powMod(base, exp, mod)
    IMPLICIT NONE
    INTEGER(KIND=8), INTENT(IN) :: base, exp, mod  ! Declara las variables de entrada
    INTEGER(KIND=8) :: result                      ! Resultado de la exponenciación modular

    result = 1_8  ! Establece el valor inicial de result

    ! Bucle para calcular la exponenciación modular
    DO WHILE (exp > 0)
        IF (MOD(exp,2_8) == 1) THEN
            result = MOD(result * base, mod)
        END IF
        base = MOD(base * base, mod)  ! Eleva al cuadrado la base
        exp = exp / 2_8               ! Divide el exponente por 2
    END DO

    powMod = result  ! Devuelve el resultado
    RETURN
END FUNCTION powMod
