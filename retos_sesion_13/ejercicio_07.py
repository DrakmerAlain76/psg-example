# Crear una serie de números del 1 al 100, si el número es divisible entre 5 imprimir Fizz, si el número es divisible entre 7 imprimir Buzz, si el número es divisible entre 5 y 7 imprimir FizzBuzz
for i in range(1, 101):
    if i % 5 == 0 and i % 7 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Fizz")
    elif i % 7 == 0:
        print("Buzz")
    else:
        print(i)
