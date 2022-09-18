############################################################################
#Codigo Python para estudo 
#Usando modulo criado para esse código, menu e loop
#Exemplo utilizado do site Python Progressivo - Tutorial Importar Modulo
#
#Data: 2022-09-13
#Ajustei com a opção de sair do loop do site Delf Stack
#Os links das fontes estão no final do arquivo
#
#Data: 2022-09-16
#Ajustei o modulo calcular.py
#Adicionei as funcoes de raiz e potencia
#Ajustes no codigo calculadora.py adicionando as entradas e algoritmo que 
#busca essas funcoes no modulo 
#
#Data: 2022-09-17
#Corrigido o erro groseiro de posicao dos itens 5 e 6 e da variavel
#que agora ficou como z e para cada operacao 5 e 6 está apontada diretamente
#
#Mario Medeiros - Disaster Developer
#
#############################################################################

import calcular

while True:
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Raiz")
    print("6. Potencia")
    print("00. Sair")
  
    op=int(input("Que operação deseja realizar: "))

    ###################################################
    #O bloco if abaixo faz a "quebra" o loop dando a opcao de saida do programa
    #a posicao desse if/break deve ser antes do inicio do codigo evitando
    #que seja ignorado ou que precise passar por outras partes primeiro
    ###################################################

    if op==00:
        break

    ########################
    #O bloco if abaixo da a opcao de inserir somente um numero para os calculos
    #de raiz ou potencia
    #######################    
        
    if op==5:
        z=float(input("Número à Calcular: "))
        print("Raiz:", calcular.raiz(z))
    elif op==6:
        z=float(input("Número à Calcular: "))
        print("Potência:", calcular.potencia(z))
   
    else:
        x=float(input("Primeiro numero: "))
        y=float(input("Segundo  numero: "))

    if op==1:
        print("Soma:", calcular.soma(x,y))
    elif op==2:
        print("Subtração:", calcular.subtracao(x,y))
    elif op==3:
        print("Multiplicação:", calcular.multiplicacao(x,y))
    elif op==4:
        print("Divisão:", calcular.divisao(x,y))
      
#Fonte: https://www.pythonprogressivo.net/2018/07/import-Como-Criar-Importar-Usar-Modulo-Python-Curso.html
# 
#Fonte referente a parte do codigo que sai do loop - break
#https://www.delftstack.com/howto/python/python-text-menu-infinite-loop/
