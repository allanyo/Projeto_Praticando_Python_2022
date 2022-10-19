
""" esse codigo é para mostrar se um numero é PAR ou IMPA"""
num = int(input("Digite um numero: "))





def Par_ou_Impar(num): #utilizando uma função
  
    if (num % 2) == 0: 
        print("\nEsse numero é PAR\n")
    else:
        print("\nEsse numero é IMPAR\n")

Par_ou_Impar(num)