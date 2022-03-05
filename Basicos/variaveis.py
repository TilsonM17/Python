# Operações a ser feitas(+ - * /) tem as particulares[//,**] 
#  ** - Potencia
# // - Divisão mais ignora o ponto flutuante

nome = input('Digite o seu nome:')
nota1 =int(input('Diga a primeira nota:'))
nota2 = int(input('Diga a segunda nota:'))

media = (nota1+nota2)//2

print('Ola',nome,'A sua media',int(media))