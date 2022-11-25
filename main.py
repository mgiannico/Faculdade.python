# ENUNCIADO DA QUESTÃO 1
# Faça um algoritmo que receba três valores, representando os lados de um triângulo fornecidos pelo usuário. Verifique se os valores formam um triângulo e classifique como:
# a) Equilátero (três lados iguais)
# b) Isósceles (dois lados iguais)
# c) Escaleno (três lados diferentes)
# Lembre-se de que, para formar um triângulo, nenhum dos lados pode ser igual a zero, e um lado não pode ser maior do que a soma dos outros dois (exercício da apostila – aula 3)


lado1 = int(input('Digite o primeiro tamanho do lado do triângulo: '))
lado2 = int(input('Digite o segundo tamanho do lado do triângulo: '))
lado3 = int(input('Digite o terceiro tamanho do lado do triângulo: '))

if (lado1 > 0) and (lado2 > 0) and (lado3 >0):
    if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado3 + lado2 > lado1):
        #se você chegou até aqui é pq o triângulo é válido
        if (lado1 != lado2) and (lado1 != lado3) and (lado2 != lado3):
            print('Triângulo escaleno')
        else:
            if (lado1 == lado2) and (lado1 == lado3) and (lado2 == lado3):
                print('Triângulo Equilátero')
            else:
                print('Triângulo Isósceles')
    else:
        print('Ao menos um dos valores não servem para formar um triângulo')
else:
    print('Ao menos um dos valores não servem para formar um triângulo')