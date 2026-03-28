# lendo os números reais
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))
n4 = float(input("Digite o quarto número: "))
# média
media = (n1 + n2 + n3 + n4) / 4
# maior e menor
maior = max(n1, n2, n3, n4)
menor = min(n1, n2, n3, n4)
# diferença
diferenca = maior - menor
# resultado
print(f"A média é {media} e a diferença entre o maior e o menor é {diferenca}")