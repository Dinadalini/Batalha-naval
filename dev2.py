import random

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

# quantidade de blocos por modelo de navio
CONFIGURACAO = {
    'destroyer': 3,
    'porta-avioes': 5,
    'submarino': 2,
    'torpedeiro': 3,
    'cruzador': 2,
    'couracado': 4
}
#países e seus números
PAISES= {
    1: 'Brasil',
    2: 'Coreia do Norte',
    3: 'Vaticano',
    4: 'Tibet',
    5: 'China',
    6: 'Estados Unidos',
    7: 'Inglaterra',
    8: 'Bahamas',
    9: 'México',
    10: 'Emirados Árabes Unidos'
}

#separação entre o tabuleiro e os países
print("-------------------------")

#print dos paises
print("1: Brasil\n2: Coreia do Norte\n3: Vaticano\n4: Tibet\n5: China\n6: Estados Unidos\n7: Inglaterra\n8: Bahamas\n9: México\n10: Emirados Árabes Unidos")


#Jogador vai escolher o seu país
def jogador_escolhe_pais():
    for num, pais in PAISES.items():
        print(f'{num}. {pais}')
    escolha_numero_pais= int(input("Digite o número de nação que você irá defender: "))
    if escolha_numero_pais in PAISES: 
        return PAISES[escolha_numero_pais]
    else:
        print("Nação desconhecida. Digite um número válido")
    return jogador_escolhe_pais()

#computador escolhe um país diferente do jogador aleatoriamente e printa o pais escolhido
def computador_escolhe_pais():
    paises_disponiveis_comp= list(PAISES.value())
    paises_disponiveis_comp.remove(jogador_escolhe_pais)
    escolha_do_pais_computador= random.choice(paises_disponiveis_comp)
    print(f'O computador escolheu o país: {escolha_do_pais_computador}')
    return escolha_do_pais_computador