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
#Mario Medeiros - Disaster Developer
#
#############################################################################
#############################################################################
# Esse módulo realiza as 4 operações matemáticas
#
# Alterado o modulo em 2022-09-16 - para estudos
# Esse módulo realiza as 6 operações matemáticas
#
#############################################################################
#
#Data: 2022-09-17
#Ajustes na variável utilizada nas funcoes de raiz e potência
#Alterada de x para z. Devido ao algoritmo do arquivo calculadora.py
#
#
#############################################################################
# Recebe dois números e retorna a soma
def soma(x,y):
    return x+y

# Recebe dois números e retorna a diferença
def subtracao(x,y):
    return x-y

# Recebe dois números e retorna o produto
def multiplicacao(x,y):
    return x*y

# Recebe dois números e retorna a divisão do primeiro pelo segundo
def divisao(x,y):
    return x/y

#Recebe o numero z e calcula a raiz quadrada - funcao que adicionei e mudei de x para z
def raiz(z):
    return (z ** (0.5))

#Recebe o numero z e calcula a potencia quadrada - funcao que adicionei e mudei de x para z
def potencia(z):
    return z*z
    
#Fonte: https://www.pythonprogressivo.net/2018/07/import-Como-Criar-Importar-Usar-Modulo-Python-Curso.html    
