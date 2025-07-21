# calculadora.py

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero"

print("Calculadora básica 21 de julio primera rama 1")
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

print("Operaciones disponibles: +, -, *, /")
operacion = input("Seleccione una operación: ")

if operacion == "+":
    print("Resultado:", sumar(num1, num2))
elif operacion == "-":
    print("Resultado:", restar(num1, num2))
elif operacion == "*":
    print("Resultado:", multiplicar(num1, num2))
elif operacion == "/":
    print("Resultado:", dividir(num1, num2))
else:
    print("Operación no válida.")
