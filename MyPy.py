#testes de comantário

import os #importa cmd
os.system ('cls')
os.system('echo.')

#MODELOS DE VARIÁVIES
a = "Hello World"
b = [5,4,3,2,1]
c = ['nenhum','MAÇÃS','PERAS','UVAS','BANANAS','LARANJAS']
d = ['ninguem','MONICA','CEBOLINHA', 'CASCAO', 'FRANJINHA','MAGALI']

#DEFINIR TIPO DE DADOS
#	a=str(a) - para string
#	b=int(b) - para inteiros
#
#
#



#REPETIÇÃO COM  FOR...IN...PRINT
for i in range(5):
   print (a)
   print (b[i])
   print (c[i])
print (i)  #Nota: Deve estar estruturado
print("\n")

#laço de repetição WHILE
# nome = input ('Insira um Nome: ')
# while nome: #só sai do looping quando NOME=vasio
#   nome = input ('Insira um Nome: ')

#EXEMPLO
nome = 'marcelo '
sobre1 = ' de oliveira '
sobre2 = ' honorio'
print(nome+sobre1+sobre2)
print("\n")


#EXEMPLO
n = input ('Sorteie alguém, num de 1 a 5 :' )
n = int(n)
f = input ('Sorteie uma fruta de 1 a 5 :' )
f = int(f)
p = (n*f)
p = int(p)
print (d[n], "comprou", p, c[f], "na feira.")
print("\n")

 
Nome = "lelo"
cumprimento = "Olá, " + Nome
print (cumprimento)
print("\n")
   
exit()