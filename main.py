#Exemplo que causa TypeError

nome = "Adriano"
try:
    resultado = len(3)
    print(resultado)
except TypeError as e:
    print(e)
else:
    print("tudo ocorreu bem")
finally:
    print("o importante é participar")  

numero = int(input("Insira um numero :"))
if isinstance(numero, int):
    print("A variável é um inteiro.")
else:
    print("A variável não é um inteiro.")