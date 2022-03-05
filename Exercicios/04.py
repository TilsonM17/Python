#Faca um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
#e todas as info sobre ele

algo = input('Digite qualquer coisa: ')
# print('''\
# -----------------INFO SOBRE O ITEM DIGITADO----------------------
# ******************************************************************
# TIPO:{0}
# É ALFHA NUMERIC : {1}
# É MINUSCULO : {2}
# É TITLECASE : {3}



# ******************************************************************
# ---------------------------FIM------------------------------------

# '''.format(type(algo),algo.isalnum(),algo.islower(),algo.istitle()))



#NOTA: No python 3.7 não necessita do format ataz podemos usar a sintaxe abaixo:
print(f'O tipo da frase : {type(algo)}')