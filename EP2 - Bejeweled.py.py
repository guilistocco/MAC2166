"""
  AO PREENCHER ESSE CABEÇALHO COM O MEU NOME E O MEU NÚMERO USP,
  DECLARO QUE SOU A ÚNICA PESSOA AUTORA E RESPONSÁVEL POR ESSE PROGRAMA.
  TODAS AS PARTES ORIGINAIS DESSE EXERCÍCIO PROGRAMA (EP) FORAM
  DESENVOLVIDAS E IMPLEMENTADAS POR MIM SEGUINDO AS INSTRUÇÕES
  DESSE EP E, PORTANTO, NÃO CONSTITUEM ATO DE DESONESTIDADE ACADÊMICA,
  FALTA DE ÉTICA OU PLÁGIO.
  DECLARO TAMBÉM QUE SOU A PESSOA RESPONSÁVEL POR TODAS AS CÓPIAS
  DESSE PROGRAMA E QUE NÃO DISTRIBUÍ OU FACILITEI A
  SUA DISTRIBUIÇÃO. ESTOU CIENTE QUE OS CASOS DE PLÁGIO E
  DESONESTIDADE ACADÊMICA SERÃO TRATADOS SEGUNDO OS CRITÉRIOS
  DIVULGADOS NA PÁGINA DA DISCIPLINA.
  ENTENDO QUE EPS SEM ASSINATURA NÃO SERÃO CORRIGIDOS E,
  AINDA ASSIM, PODERÃO SER PUNIDOS POR DESONESTIDADE ACADÊMICA.

  Nome :Guilherme Mazzuia Stocco
  NUSP :10332886
  Turma:06
  Prof.:Kelly Rosa Braghetto

  Referências: Com exceção das rotinas fornecidas no enunciado
  e em sala de aula, caso você tenha utilizado alguma referência,
  liste-as abaixo para que o seu programa não seja considerado
  plágio ou irregular.

  Exemplo:
  - O algoritmo Quicksort foi baseado em
  https://pt.wikipedia.org/wiki/Quicksort
  http://www.ime.usp.br/~pf/algoritmos/aulas/quick.html
"""
# ======================================================================
#
#   FUNÇÕES FORNECIDAS: NÃO DEVEM SER MODIFICADAS
#
# ======================================================================
import random
random.seed(0)

def main():
    '''
    Esta é a função principal do seu programa. Ela contém os comandos que
    obtêm os parâmetros necessários para criação do jogo (número de linhas,
    colunas e cores), e executa o laço principlal do jogo: ler comando,
    testar sua validade e executar comando.

    ******************************************************
    ** IMPORTANTE: ESTA FUNÇÃO NÃO DEVE SER MODIFICADA! **
    ******************************************************
    '''
    print()
    print("=================================================")
    print("             Bem-vindo ao Gemas!                 ")
    print("=================================================")
    print()

    pontos = 0
    # lê parâmetros do jogo
    num_linhas = int(input("Digite o número de linhas [3-10]: ")) # exemplo: 8
    num_colunas = int(input("Digite o número de colunas [3-10]: ")) # exemplo: 8
    num_cores = int(input("Digite o número de cores [3-26]: ")) # exemplo: 7
    # cria tabuleiro com configuração inicial
    tabuleiro = criar (num_linhas, num_colunas)
    completar (tabuleiro, num_cores)
    num_gemas = eliminar (tabuleiro)
    while num_gemas > 0:
        deslocar (tabuleiro)
        completar (tabuleiro, num_cores)
        num_gemas = eliminar (tabuleiro)
    # laço principal do jogo
    while existem_movimentos_validos (tabuleiro): # Enquanto houver movimentos válidos...
        exibir (tabuleiro)
        comando = input("Digite um comando (perm, dica, sair ou ajuda): ")
        if comando == "perm":
            linha1 = int(input("Digite a linha da primeira gema: "))
            coluna1 = int(input("Digite a coluna da primeira gema: "))
            linha2 = int(input("Digite a linha da segunda gema: "))
            coluna2 = int(input("Digite a coluna da segunda gema: "))
            print ()
            valido = trocar ( linha1, coluna1, linha2, coluna2, tabuleiro)
            if valido:
                num_gemas = eliminar (tabuleiro)
                total_gemas = 0
                while num_gemas > 0:
                    # Ao destruir gemas, as gemas superiores são deslocadas para "baixo",
                    # criando a possibilidade de que novas cadeias surjam.
                    # Devemos então deslocar gemas e destruir cadeias enquanto houverem.
                    deslocar (tabuleiro)
                    completar (tabuleiro, num_cores)
                    total_gemas += num_gemas
                    print("Nesta rodada: %d gemas destruidas!" % num_gemas )
                    exibir (tabuleiro)
                    num_gemas = eliminar (tabuleiro)
                pontos += total_gemas
                print ()
                print ("*** Você destruiu %d gemas! ***" % (total_gemas))
                print ()
            else:
                print ()
                print ("*** Movimento inválido! ***")
                print ()
        elif comando == "dica":
            pontos -= 1
            linha, coluna = obter_dica (tabuleiro)
            print ()
            print ("*** Dica: Tente permutar a gema na linha %d e coluna %d ***" % (linha, coluna))
            print ()
        elif comando == "sair":
            print ("Fim de jogo!")
            print ("Você destruiu um total de %d gemas" % (pontos))
            return
        elif comando == "ajuda":
            print("""
============= Ajuda =====================
perm:  permuta gemas
dica:  solicita uma dica (perde 1 ponto)
sair:  termina o jogo
=========================================
                  """)
        else:
            print ()
            print ("*** Comando inválido! Tente ajuda para receber uma lista de comandos válidos. ***")
            print ()
    print("*** Fim de Jogo: Não existem mais movimentos válidos! ***")
    print ("Você destruiu um total de %d gemas" % (pontos))

def completar (tabuleiro, num_cores):
    ''' (matrix, int) -> None

    Preenche espaços vazios com novas gemas geradas aleatoriamente.

    As gemas são representadas por strings 'A','B','C',..., indicando sua cor.
    '''
    alfabeto = ['A','B','C','D','E','F','G','H','I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    num_linhas = len (tabuleiro)
    num_colunas = len (tabuleiro[0])
    for i in range (num_linhas):
        for j in range (num_colunas):
            if tabuleiro[i][j] == ' ':
                gema = random.randrange (num_cores)
                tabuleiro[i][j] = alfabeto[gema]


# ======================================================================
#
#   FUNÇÕES A SEREM IMPLEMENTADAS POR VOCÊ
#
# ======================================================================

def criar (num_linhas, num_colunas):
    ''' (int,int) -> matrix

    Cria matriz de representação do tabuleiro e a preenche com
    espaços vazios representados por ' '.

    Retorna a matriz criada.
    '''
    matriz = []
    #
    for i in range(num_linhas):
        matriz.append([])
                
        for j in range(num_colunas):
            matriz[i].append(' ')
    #
    return matriz

def exibir (tabuleiro):
    ''' (matrix) -> None

    Exibe o tabuleiro.
    '''
    #
    linhas = len(tabuleiro)
    colunas = len(tabuleiro[0])

    print(end = '    ')
    for j in range(0, colunas) :
        print(j, end = ' ' ) # numeros em cima
    print()
    print(end = ' ')                      # barra em cima
    print(' +-' + ('--' * colunas) + '+')
        
    for i in range(0, linhas):            
        print(i, '| ', end = '')            
        for j in range(0, colunas) :                
            print(tabuleiro[i][j], end = " ")
        print('|')              
    print('  +-' + ('--' * colunas) + '+') # barra em baixo

def trocar (linha1, coluna1, linha2, coluna2, tabuleiro):
    ''' (int,int,int,int,matrix) -> Bool

    Permuta gemas das posições (linha1, coluna1) e (linha2, coluna2) caso
    seja válida (isto é, gemas são adjacentes e geram cadeias), caso contrário
    não altera o tabuleiro.

    Retorna `True` se permutação é válida e `False` caso contrário.
    '''
    #
    if linha1 < 0 or linha2 < 0 or coluna1 < 0 or coluna2 < 0:       # index dentro do tabuleiro
        return False
    elif linha1 > len(tabuleiro)-1 or linha2 > len(tabuleiro)-1 or coluna1 > len(tabuleiro[0])-1 or coluna2 > len(tabuleiro[0])-1 :
        return False 
    elif tabuleiro[linha1][coluna1] == tabuleiro[linha2][coluna2]:
        return False
    else :
        if linha1 < 0 or linha2 < 0 or coluna1 < 0 or coluna2 < 0:       # index dentro do tabuleiro
            return False
        elif linha1 > len(tabuleiro)-1 or linha2 > len(tabuleiro)-1 or coluna1 > len(tabuleiro[0])-1 or coluna2 > len(tabuleiro[0])-1 :
            return False 

    

        adjacente = False
        if coluna1 == coluna2 :      #sao verticais
            if linha1 == linha2+1 or linha2 == linha1+1:
                adjacente = True
            if linha1 == linha2-1 or linha2 == linha1-1:
                adjacente = True
                
        if linha1 == linha2 :        #sao horizontais
            if coluna1 == coluna2+1 or coluna2 == coluna1+1:
                adjacente = True
            if coluna1 == coluna2-1 or coluna2 == coluna1-1:
                adjacente = True


        if adjacente == False :
            return False
        else:
            aux = tabuleiro[linha1][coluna1]
            tabuleiro[linha1][coluna1] = tabuleiro[linha2][coluna2]
            tabuleiro[linha2][coluna2] = aux
            horizontais = identificar_cadeias_horizontais (tabuleiro)
            verticais = identificar_cadeias_verticais (tabuleiro)
            if len(horizontais) != 0 or len(verticais) != 0 :
                return True
            else:
                aux = tabuleiro[linha1][coluna1]
                tabuleiro[linha1][coluna1] = tabuleiro[linha2][coluna2]
                tabuleiro[linha2][coluna2] = aux
                return False

    #
    return False


def eliminar (tabuleiro):
    ''' (matrix) -> int

    Elimina cadeias de 3 ou mais gemas, substituindo-as por espaços (' ').

    Retorna número de gemas eliminadas.
    '''
    num_eliminados = 0
    #
    
    cadeias_horizontais = identificar_cadeias_horizontais(tabuleiro)
    cadeias_verticais = identificar_cadeias_verticais (tabuleiro)

    
    for i in range(len(cadeias_horizontais)) :
        num_eliminados += eliminar_cadeia (tabuleiro, cadeias_horizontais[i])

    for j in range(len(cadeias_verticais)) :
        num_eliminados += eliminar_cadeia (tabuleiro, cadeias_verticais[j])

    #
    return num_eliminados

def identificar_cadeias_horizontais (tabuleiro):
    ''' (matrix) -> list

    Retorna uma lista contendo cadeias horizontais de 3 ou mais gemas. Cada cadeia é
    representada por uma lista `[linha, coluna_i, linha, coluna_f]`, onde:

    - `linha`: o número da linha da cadeia
    - `coluna_i`: o número da coluna da gema mais à esquerda (menor) da cadeia
    - `coluna_f`: o número da coluna da gema mais à direita (maior) da cadeia

    Não modifica o tabuleiro.
    '''
    cadeias = []
    #
    for i in range(len(tabuleiro)):
        cont = 1
        for j in range(len(tabuleiro[0])):
            if j+1 <= len(tabuleiro[0])-1 and tabuleiro[i][j] == tabuleiro[i][j+1] :
                cont += 1
            else: 
                if cont < 3:
                    cont = 1
                else:
                    cadeias.append([i,j-cont+1, i, j])
                    cont = 1
    #
    return cadeias

def identificar_cadeias_verticais (tabuleiro):
    ''' (matrix) -> list

    Retorna uma lista contendo cadeias verticais de 3 ou mais gemas. Cada cadeia é
    representada por uma lista `[linha_i, coluna, linha_f, coluna]`, onde:

    - `linha_i`: o número da linha da gemas mais superior (menor) da cadeia
    - `coluna`: o número da coluna das gemas da cadeia
    - `linha_f`: o número da linha mais inferior (maior) da cadeia

    Não modifica o tabuleiro.
    '''
    cadeias = []
    #
    for j in range(len(tabuleiro[0])):
        cont = 1
        for i in range(len(tabuleiro)):
            if i+1 <= len(tabuleiro)-1 and tabuleiro[i][j] == tabuleiro[i+1][j] :
                cont += 1
            else: 
                if cont < 3:
                    cont = 1
                else:
                    cadeias.append([i-cont+1,j, i, j])
                    cont = 1
    #
    return cadeias

def eliminar_cadeia (tabuleiro, cadeia):
    ''' (matrix,list) -> int

    Elimina (substitui pela string espaço `" "`) as gemas compreendidas numa cadeia,
    representada por uma lista `[linha_inicio, coluna_inicio, linha_fim, coluna_fim]`,
    tal que:

    - `linha_i`: o número da linha da gema mais superior (menor) da cadeia
    - `coluna_i`: o número da coluna da gema mais à esquerda (menor) da cadeia
    - `linha_f`: o número da linha mais inferior (maior) da cadeia
    - `coluna_f`: o número da coluna da gema mais à direita (maior) da cadeia

    Retorna o número de gemas eliminadas.
    '''
    num_eliminados = 0
    #
    if cadeia[0] == cadeia[2]:      # cadeia horizontal
        i = cadeia[1]
        while i <= cadeia[3] :
            if tabuleiro[0][i] != ' ':
                tabuleiro[cadeia[0]][i] = ' '
                num_eliminados += 1
            i += 1

    elif cadeia[1] == cadeia[3]:    # cadeia vertical
        i = cadeia[0]
        while i <= cadeia[2] :
            if tabuleiro[i][0] != ' ':
                tabuleiro[i][cadeia[3]] = ' '
                num_eliminados += 1
            i += 1             
    #
    return num_eliminados


def deslocar (tabuleiro):
    ''' (matrix) -> None

    Desloca gemas para baixo deixando apenas espaços vazios sem nenhuma gema acima.
    '''
    #
    for i in range(len(tabuleiro[0])):
        deslocar_coluna(tabuleiro, i)

def deslocar_coluna ( tabuleiro, i ):
    ''' (matrix, int) -> None

    Desloca as gemas na coluna i para baixo, ocupando espaços vazios.
    '''
    #
    n = len(tabuleiro)
    while n > 0:
        
        k = len(tabuleiro)-1
        while k > 0 :
            if tabuleiro[k][i] == ' ':
                j = k
                while j > 0 :
                    tabuleiro[j][i] = tabuleiro[j-1][i]
                    j -= 1
                tabuleiro[0][i] = " "
            k -= 1
        n -= 1
        

def existem_movimentos_validos (tabuleiro):
    '''(matrix) -> Bool

    Retorna True se houver movimentos válidos, False caso contrário.
    '''
    #
    a,b = obter_dica (tabuleiro)
    if a == -1 and b == -1 :
        return False
    #
    return True


def obter_dica (tabuleiro):
    '''(matrix) -> int,int

    Retorna a posição (linha, coluna) de uma gema que faz parte de uma
    permutação válida.

    Se não houver permutação válida, retorne -1,-1.
    '''
    linha = -1
    coluna = -1
    #
    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro[0])):
            if trocar(i,j,i,j+1,tabuleiro) == True:
                aux = tabuleiro[i][j]
                tabuleiro[i][j] = tabuleiro[i][j+1]
                tabuleiro[i][j+1] = aux
                linha = i
                coluna = j
                return linha, coluna

            elif trocar(i,j,i+1,j,tabuleiro) == True:
                auxx = tabuleiro[i][j]
                tabuleiro[i][j] = tabuleiro[i+1][j]
                tabuleiro[i+1][j] = auxx
                linha = i
                coluna = j
                return linha, coluna
            
    #
    return linha, coluna


main()
