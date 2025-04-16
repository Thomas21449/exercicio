#def main():
 # idade=int(input("qual é a sua idade?"))
  #if idade >= 18:
   #   print("maior de idade")
    #else:
     #   print("menor de idade")

#if __name__ == '__main__':
#  main()

#numero=int(input("escolha um numero?"))
#if numero%2==0:
#     print("par")
#else:
#     print("impar")

#def par_ou_impar(numero):
#    ultimo_digito = str(numero)[-1]
#    if ultimo_digito == '0' '2','4','6','8':

'''def main():
    renda=float(input("Renda da familia?:"))
    pessoa_familia =int(input("pessoa por familia?:"))
    cad_unico=input("tem cadastro unico?: (S)im (N)ão")
    renda_pessoa=renda/pessoa_familia
    if (renda_pessoa <= 218) and (cad_unico=="S"):
        print("beneficio consedido")
    else:
        print("beneficio não consedido")

        if __name__=='__main__':
            main()'''

def bolsafamilia(renda:float,pessoas:int,cad_unico:str)->bool:
    renda_pessoa=renda/pessoas
    if (renda_pessoa <= 218) and (cad_unico.upper()=="S"):
        return True
    else:
        return False

def main():
    renda=float(input("Renda da familia?:"))
    pessoa_familia =int(input("pessoa por familia?:"))
    cad_unico=input("tem cadastro unico?: (S)im (N)ão")
    if bolsafamilia(renda,pessoa_familia,cad_unico):
        print("consedido")
    else:
        print("não consedido")

if __name__=='__main__':
    main()