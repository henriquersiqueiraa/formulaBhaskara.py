import math

def calcula_raizes(a, b, c):
    # Calcula o discriminante
    delta = b**2 - 4*a*c
    
    # Verifica se não há raízes reais
    if delta < 0:
        print("esta equação não possui raízes reais")
    # Verifica se há uma raiz dupla
    elif delta == 0:
        raiz = -b / (2*a)
        print(f"a raiz dupla desta equação é {raiz}")
    # Calcula as duas raízes reais distintas
    else:
        raiz1 = (-b - math.sqrt(delta)) / (2*a)
        raiz2 = (-b + math.sqrt(delta)) / (2*a)
        # Ordena as raízes em ordem crescente
        if raiz1 > raiz2:
            raiz1, raiz2 = raiz2, raiz1
        print(f"as raízes da equação são {raiz1} e {raiz2}")

# Exemplo de uso
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

calcula_raizes(a, b, c)