# Modulo for calculations
MOD <- 1000000007

# Propiedad de Exponenciación:
# Para la exponenciación modular, donde queremos calcular a^b \mod ma 
# b
#  modm, utilizamos un algoritmo eficiente que explota las propiedades del operador módulo.

# La exponenciación modular se basa en las siguientes observaciones:

# (a \cdot b) \mod m = ((a \mod m) \cdot (b \mod m)) \mod m(a⋅b)modm=((amodm)⋅(bmodm))modm
# (a \cdot b) \cdot c \mod m = ((a \mod m) \cdot (b \mod m) \cdot (c \mod m)) \mod m(a⋅b)⋅cmodm=((amodm)⋅(bmodm)⋅(cmodm))modm
# Entonces, para calcular a^b \mod ma 
# b
#  modm, el algoritmo es algo como esto (usando una versión de la exponenciación binaria):

# Inicializar un resultado a 11.
# Mientras b > 0b>0:
# Si bb es impar, entonces multiplicar el resultado por aa y tomar \mod mmodm.
# Dividir bb por 22 (o realizar un desplazamiento hacia la derecha si estamos trabajando en nivel de bits).
# Elevar aa al cuadrado y tomar \mod mmodm.
# El resultado final es a^b \mod ma 
# b
#  modm.
# Así, el algoritmo utiliza la propiedad de que puedes tomar el módulo en cada paso del cálculo sin afectar el resultado final.

# A function to calculate the power of a number modulo MOD
# Time Complexity: O(log(exp))
# Space Complexity: O(1)
power <- function(base, exp) {
  result <- 1
  while (exp > 0) {
    if (exp %% 2 == 1) {
      result <- (result * base) %% MOD  # Multiply the result by base if exp is odd
    }
    base <- (base * base) %% MOD  # Square the base
    exp <- exp %/% 2  # Divide the exponent by 2
  }
  return(result)
}

# A function to compute S(k) in a non-modular space
# Time Complexity: O(log(k))
# Space Complexity: O(1)
S <- function(k) {
  n <- k %/% 9
  r <- k %% 9 + 2
  return((((r - 1) * r + 10) * power(10, n) - 2 * (r + 9 * n + 4)) %/% 2)
}

# A function to compute S(k) in a modular space
# Time Complexity: O(log(k))
# Space Complexity: O(1)
modular_S <- function(k) {
  n <- k %/% 9
  r <- k %% 9 + 2
  return((((r - 1) * r + 10) * power(10, n) - 2 * (r + 9 * n + 4)) * power(2, MOD - 2) %% MOD)
}

# A function to generate Fibonacci numbers up to n
# Time Complexity: O(n)
# Space Complexity: O(n)
fib <- function(n) {
  fib_numbers <- numeric(n)
  a <- 0
  b <- 1
  for (i in seq_len(n)) {
    fib_numbers[i] <- a
    temp <- a
    a <- b
    b <- temp + b
  }
  return(fib_numbers)
}

# The main function to compute the result
# Time Complexity: O(n*log(k)) where n is the number of Fibonacci numbers and k is the Fibonacci number
# Space Complexity: O(n)
main <- function() {
  # Testing the functions
  stopifnot(S(20) == 1074)
  stopifnot(S(49) == 1999945)
  stopifnot(modular_S(20) == 1074)
  stopifnot(modular_S(49) == 1999945)

  # Calculating the result
  n <- 91
  fib_numbers <- fib(n)
  result <- 0
  for (i in seq(3, n)) {
    result <- (result + modular_S(fib_numbers[i])) %% MOD
  }
  cat("Result:", result, "\n")
}

# Calling the main function
main()
