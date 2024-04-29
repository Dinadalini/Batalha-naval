def criar_tabuleiro():
    colunas=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    linhas= list(range(1, 11))
    tabuleiro= [['' for i in colunas] for i in linhas]
    return tabuleiro

def imprimir_tabuleiro (tabuleiro):
    colunas = [' A', ' B', ' C', ' D', ' E', ' F', ' G', ' H', ' I', ' J']
    print ('  '+ '  '.join(colunas))
    for j, linha in enumerate(tabuleiro, start=1):
        print(f'{j:2}'+ '   '.join(linha))

tabuleiro_computador= criar_tabuleiro()
tabuleiro_jogador= criar_tabuleiro()

print ("tabuleiro Computador:")
imprimir_tabuleiro(tabuleiro_computador)
print ("tabuleiro Jogador:")
imprimir_tabuleiro(tabuleiro_jogador)
