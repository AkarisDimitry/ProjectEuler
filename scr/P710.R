MOD <- 1000000

# Función para calcular potencia con módulo
pow_mod <- function(base, exponent, mod_val) {
  result <- 1
  base <- base %% mod_val

  while (exponent > 0) {
    if (exponent %% 2 == 1) {
      result <- (result * base) %% mod_val
    }
    base <- (base * base) %% mod_val
    exponent <- exponent %/% 2
  }

  return(result %% mod_val)
}

# Función principal para calcular el valor deseado
P710 <- function() {
  pal_odd <- 0
  pal_odd_0b2 <- 2
  pal_odd_0b4 <- 1
  two_pal_odd <- 0
  two_pal_odd_0b2 <- 1
  two_pal_odd_0b4 <- 0
  two_pal <- 0
  suma_odd <- 0
  suma_even <- 0
  n <- 2

  while (two_pal %% MOD != 0 || n < 42) {
    n <- n + 2
    pal_odd <- pow_mod(2, n/2 - 1, MOD)
    two_pal_odd <- (suma_odd - two_pal_odd_0b4 + pal_odd_0b4) %% MOD
    two_pal <- (two_pal_odd + suma_even - two_pal_odd_0b2 + pal_odd_0b2) %% MOD

    suma_odd <- suma_odd + two_pal_odd
    suma_even <- suma_even + two_pal_odd

    pal_odd_0b4 <- pal_odd_0b2
    pal_odd_0b2 <- pal_odd
    two_pal_odd_0b4 <- two_pal_odd_0b2
    two_pal_odd_0b2 <- two_pal_odd
  }

  return(n)
}

# Ejecuta la función y muestra el resultado
result <- P710()
cat("Result of P710:", result, "\n")
