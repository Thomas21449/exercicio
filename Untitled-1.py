while True:
    try:
      produto = float(input("informe o valor do produto:"))
      pago = float(input("informe o valor pago:"))
      troco = pago-produto
      print(f'O troco é de R$ {troco:.2f}')
      break
    except ValueError:
     print("deve ser um valor floate!!")