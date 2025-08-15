def main():
  print("Hello learners!")

if __name__=="__main__":
  main()

  def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: División por cero"
    return a / b

# --- Funciones adicionales ---
def addmultiplenumbers(lista):
    """Suma todos los números de una lista y regresa el resultado."""
    return sum(lista)

def multiplymultiplenumbers(lista):
    """Multiplica todos los números de una lista y regresa el resultado."""
    resultado = 1
    for num in lista:
        resultado *= num
    return resultado

def isiteven(numero):
    """Regresa True si el número es par (y entero), o False si no."""
    return isinstance(numero, int) and numero % 2 == 0

def isitaninteger(numero):
    """Regresa True si el número es entero (por ejemplo 7 o 7.0), o False si no."""
    return numero == int(numero)

# --- Ejemplo de uso ---
if __name__ == "__main__":
    print("Funciones básicas:")
    print("Suma:", sumar(5, 3))
    print("Resta:", restar(10, 4))
    print("Multiplicación:", multiplicar(2, 6))
    print("División:", dividir(8, 2))

    print("\nFunciones adicionales:")
    print("Suma múltiple:", addmultiplenumbers([1, 2, 3, 4]))
    print("Multiplicación múltiple:", multiplymultiplenumbers([1, 2, 3, 4]))
    print("¿Es par?", isiteven(4))
    print("¿Es entero?", isitaninteger(7.0))

    # --- Pruebas ---
print("Pruebas isiteven:")
print(isiteven(4))      # True
print(isiteven(7))      # False
print(isiteven(4.0))    # False
print(isiteven(-8))     # True
print(isiteven(3.5))    # False

print("\nPruebas isitaninteger:")
print(isitaninteger(7))     # True
print(isitaninteger(7.0))   # True
print(isitaninteger(3.5))   # False
print(isitaninteger(-2))    # True
print(isitaninteger("5"))   # Error o False dependiendo del tipo