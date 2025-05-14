numero = int(input("Digite seu número e vou transformar em fatorial: "))
n = numero
resultado = 1

while n > 1:
    resultado *= n
    n -= 1

print(f"O fatorial de {numero} é {resultado}")
