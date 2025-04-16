
 def main():

             valor_total = float(input("Digite o valor da compra: "))
             if valor_total >= 100 and valor_total <= 200:
                 desconto = valor_total * 0.02
                 novoValor = valor_total - desconto
             elif valor_total <=300:
                 desconto = valor_total * 0.03
                 novoValor = valor_total - desconto
             elif valor_total <= 400:
                 desconto = valor_total * 0.4
                 novoValor = valor_total - desconto
             elif valor_total >= 400:
                 desconto = valor_total * 0.5
                 novoValor = valor_total - desconto
             else:
                 desconto = 0
                 novoValor = valor_total
             print(f'valor da compra: R${valor_total:.2f}')

             print(f'valor do desconto: {desconto:.2f}')

             print(f'valor a pagar: R${valor_total:.2f}')

if __name__ == '__main__':
    main()