
def extended_gcd(a, b):   
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = extended_gcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise ValueError('Inverso modular no existe')
    else:
        return x % m

a = 1504170715041707
m = 4503599627370517
am_inv = modinv(a=a, m=m)

def compute():
    '''
    Bottom to top search: See Equation (2) below:

    The last Eulercoin will be 1 when n = 3451657199285664, but we can reverse this 
    process, if we increase the possible Eulercoin and check if n = 3451657199285664*
    (possible Eulercoin) mod(4503599627370517) is smaller than the previous n

    For example lets test Eulercoin = 2 =>3451657199285664*(2) mod(4503599627370517)
     = 2399714771200811, and 2399714771200811 < 3451657199285664, this means that 2 
     is also an Eulercoin

    This way we only need to check Eulercoin from 1 to 15806432, which is very manageable!

    ######################################

    Vamos a descomponer esto para que sea más claro.

    La relación entre la búsqueda de \( x \) y la búsqueda de \( n \) se basa en las 
    propiedades del inverso modular. Si dos números son inversos modulares entre sí 
    con respecto a un módulo, multiplicarlos resultará en 1 (módulo ese módulo). En 
    este caso, \( 1504170715041707 \) y \( 3451657199285664 \) son inversos modulares
     con respecto a \( 4503599627370517 \). Esto significa que:

    \[
    1504170715041707 \times 3451657199285664 \equiv 1 \mod 4503599627370517
    \]

    Esto es fundamental para entender la relación entre las dos búsquedas.

    Ahora, cuando buscas "de arriba hacia abajo", estás incrementando \( n \) y 
    calculando:

    \[
    x = 1504170715041707 \times n \mod 4503599627370517
    \]

    Esto te da los valores de \( x \) en orden, y estás buscando los que son más 
    pequeños que el mínimo anterior.

    Cuando cambias a la búsqueda "de abajo hacia arriba", estás tratando de aprovechar
     el inverso modular. Dado que sabes que el último Eulercoin es 1 cuando \( 
     n = 3451657199285664 \), puedes usar este \( n \) para "predecir" cuál será el 
     próximo Eulercoin. Haces esto multiplicando el \( n \) por un "posible Eulercoin"
      y tomando el módulo con \( 4503599627370517 \). Si el resultado es menor que el 
      \( n \) anterior, entonces ese "posible Eulercoin" es en efecto un Eulercoin.

    El truco aquí es que estás utilizando la propiedad del inverso modular para "invertir"
     el cálculo. En lugar de aumentar \( n \) y ver cómo cambia \( x \), estás fijando
      \( x \) (como un "posible Eulercoin") y viendo cómo cambia \( n \). Esta inversión 
      es lo que te permite buscar de manera eficiente en el espacio de posibles Eulercoins
       en lugar de en el espacio mucho más grande de posibles valores de \( n \).

    La razón por la que solo necesitas buscar hasta 15806432 es porque ese es el valor 
    más pequeño que encontraste en la búsqueda "de arriba hacia abajo". Cualquier Eulercoin
     que sea mayor que ese valor ya habría sido encontrado en la búsqueda "de arriba hacia
     abajo", por lo que no es necesario buscar más allá de ese punto en la búsqueda "de
     abajo hacia arriba".
    '''
    eulercoins = [1504170715041707]
    current_eulercoin = 1504170715041707
    inv = pow(1504170715041707, 4503599627370517-2, 4503599627370517) # inv = pow(1504170715041707, -1, 4503599627370517)
    n = 2
    while True:
        number = 1504170715041707*n % 4503599627370517 #Search downwards
        if number < current_eulercoin:
            current_eulercoin = number
            eulercoins.append(number)
            
        if current_eulercoin == 15806432: #Our switch strategy case
            new_curr_eulercoin = 1
            curr_max = 4503599627370517
            while new_curr_eulercoin != 15806432: 
                number = (inv*new_curr_eulercoin) % 4503599627370517 #Search upwards
                if number < curr_max:
                    curr_max = number
                    eulercoins.append(new_curr_eulercoin)
                new_curr_eulercoin += 1
            break
        n += 1
        
    return sum(eulercoins)

result = compute()
print(result)
