notas = []

while True:
  valor = float(input("Informe a nota obtida na avaliação. Para finalizar, digite -1:"))
  if valor!=-1:
    notas.append(valor)
  else:
    break
print(f'A maior nota foi: {max(notas)}')
print(f'A menor nota foi: {min(notas)}')
print(f'A média das notas foi: {sum(notas)/len(notas)}')