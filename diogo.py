#importa o random pro computador escolher o país dela
import random

# Cores para o terminal
CORES = {
    'reset': '\u001b[0m',
    'red': '\u001b[31m',
    'black': '\u001b[30m',
    'green': '\u001b[32m',
    'yellow': '\u001b[33m',
    'blue': '\u001b[34m',
    'magenta': '\u001b[35m',
    'cyan': '\u001b[36m',
    'white': '\u001b[37m'
}

#cria o tabuleiro 
def criar_tabuleiro():
    colunas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    linhas = list(range(1, 11))
    tabuleiro = [[' ' for _ in colunas] for _ in linhas]
    return tabuleiro
#define o tabuleiro do jogador e do comp lado a lado
def imprimir_tabuleiros_lado_a_lado(tabuleiro_jogador, tabuleiro_computador):
    colunas = ['A', ' B', ' C', ' D', ' E', ' F', ' G', ' H', ' I', ' J']
    cabecalho = ' ' + '  '.join(colunas)
    print(f"    {cabecalho}          {cabecalho}")
    for i, (linha_jogador, linha_computador) in enumerate(zip(tabuleiro_jogador, tabuleiro_computador), start=1):
        linha_jogador_formatada = '   '.join(linha_jogador)
        linha_computador_formatada = '   '.join(linha_computador)
        print(f"{i:2}  {linha_jogador_formatada}        {i:2}  {linha_computador_formatada}")

tabuleiro_computador = criar_tabuleiro()
tabuleiro_jogador = criar_tabuleiro()

# Imprime os tabuleiros lado a lado
imprimir_tabuleiros_lado_a_lado(tabuleiro_jogador, tabuleiro_computador)

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
print("----------------------------------------------------------------------------------------------------")

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
            pais_escolhido = PAISES[escolha_numero_pais]
            print(f"Você irá defender o país {pais_escolhido}")
            return pais_escolhido
        else:
            print("Nação desconhecida. Digite um número válido.")

# Computador escolhe um país diferente do jogador aleatoriamente e printa o país escolhido
def computador_escolhe_pais(pais_jogador):
    paises_disponiveis_comp = list(PAISES.values())
    paises_disponiveis_comp.remove(pais_jogador)
    escolha_do_pais_computador = random.choice(paises_disponiveis_comp)
    print(f'O computador escolheu o país {escolha_do_pais_computador}')
    return escolha_do_pais_computador

# Programa principal
if __name__ == "__main__":
    pais_jogador = jogador_escolhe_pais()
    pais_computador = computador_escolhe_pais(pais_jogador)