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

# frotas de cada pais
PAISES_FROTAS =  {
    '1: Brasil': {
        'cruzador': 1,
        'torpedeiro': 2,
        'destroyer': 1,
        'couracado': 1,
        'porta-avioes': 1
    }, 
    '2: Coreia do Norte': {
        'cruzador': 3, 
        'porta-avioes': 1, 
        'destroyer': 1, 
        'submarino': 1, 
        'couracado': 1
    },
    '3: Vaticano': {
        'couracado': 1,
        'cruzador': 3, 
        'submarino': 1,
        'porta-avioes': 1, 
        'torpedeiro': 1
    },
    '4: Tibet': {
        'cruzador': 1,
        'porta-avioes': 1,
        'couracado': 2,
        'destroyer': 1,
        'submarino': 1
    },
    '5: China': {
        'torpedeiro': 2,
        'cruzador': 1,
        'destroyer': 2,
        'couracado': 1,
        'submarino': 1
    },
    '6: Estados Unidos': {
        'cruzador': 1,
        'torpedeiro': 2,
        'destroyer': 1,
        'couracado': 1,
        'porta-avioes': 1
    }, 
    '7: Inglaterra': {
        'cruzador': 3, 
        'porta-avioes': 1, 
        'destroyer': 1, 
        'submarino': 1, 
        'couracado': 1
    },
    '8: Bahamas': {
        'couracado': 1,
        'cruzador': 3, 
        'submarino': 1,
        'porta-avioes': 1, 
        'torpedeiro': 1
    },
    '9: México': {
        'cruzador': 1,
        'porta-avioes': 1,
        'couracado': 2,
        'destroyer': 1,
        'submarino': 1
    },
    '10: Emirados Árabes Unidos': {
        'torpedeiro': 2,
        'cruzador': 1,
        'destroyer': 2,
        'couracado': 1,
        'submarino': 1
    }
}


#Jogador vai escolher o seu país
def jogador_escolhe_pais():
    while True:
        for num, pais in PAISES_FROTAS.items():
            print(f'{num}. {pais}')
        escolha_numero_pais = int(input("Digite o número de nação que você irá defender: "))
        if escolha_numero_pais in PAISES:
            return PAISES[escolha_numero_pais]
        else:
            print("Nação desconhecida. Digite um número válido.")

# Computador escolhe um país diferente do jogador aleatoriamente e printa o país escolhido
def computador_escolhe_pais(pais_jogador):
    paises_disponiveis_comp = list(PAISES.values())
    paises_disponiveis_comp.remove(pais_jogador)
    escolha_do_pais_computador = random.choice(paises_disponiveis_comp)
    print(f'O computador escolheu o país: {escolha_do_pais_computador}')
    return escolha_do_pais_computador

# Programa principal
if __name__ == "__main__":
    pais_jogador = jogador_escolhe_pais()
    pais_computador = computador_escolhe_pais(pais_jogador)