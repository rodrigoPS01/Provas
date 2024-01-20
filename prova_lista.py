pares = []

impares = []

soma_pares = 0

soma_impares = 0

for i in range(10):
    n1 = int(input('Digite um número: '))

    if n1 % 2 == 0:
        pares.append(n1)
    else:
        impares.append(n1)

for i in pares:
    soma_pares += i

for x in impares:
    soma_impares += x

print(f'''  Tabela dos Pares
      Números: {pares}
      Quantia de números: {len(pares)}
      Soma: {soma_pares}''')

print(f'''  Tabela do ímpares
      Números: {impares}
      Quantia de números: {len(impares)}
      Soma: {soma_impares}''')