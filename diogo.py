# Importa as bibliotecas necessárias para o computador
import random
import time
from colorama import Fore, Back, Style, init
init(autoreset=True)

# Cores para o terminal
CORES = {
    'reset': Style.RESET_ALL,
    'red': Fore.RED,
    'black': Fore.BLACK,
    'green': Back.GREEN,
    'yellow': Fore.YELLOW,
    'blue': Fore.BLUE,
    'magenta': Fore.MAGENTA,
    'cyan': Fore.CYAN,
    'white': Fore.WHITE
}

# Cria o tabuleiro 
def criar_tabuleiro():
    colunas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    linhas = list(range(1, 11))
    tabuleiro = [[' ' for _ in colunas] for _ in linhas]
    return tabuleiro

# Define o tabuleiro do jogador e do comp lado a lado
def imprimir_tabuleiros_lado_a_lado(tabuleiro_jogador, tabuleiro_computador):
    colunas = [' A', ' B', ' C', ' D', ' E', ' F', ' G', ' H', ' I', ' J']
    cabecalho = ' ' + '  '.join(colunas)
    print(f"  {cabecalho}            {cabecalho}")
    for i, (linha_jogador, linha_computador) in enumerate(zip(tabuleiro_jogador, tabuleiro_computador), start=1):
        linha_jogador_formatada = '   '.join(linha_jogador) + CORES['reset']
        # Oculta os barcos do computador substituindo 'O' por ' '
        linha_computador_formatada = '  '.join([' ' if celula == 'O' else celula for celula in linha_computador]) + CORES['reset']
        print(f"{i:2}  {linha_jogador_formatada:<{len(linha_jogador_formatada)+2}}        {i:2}  {linha_computador_formatada}")



tabuleiro_computador = criar_tabuleiro()
tabuleiro_jogador = criar_tabuleiro()

# Imprime os tabuleiros lado a lado
imprimir_tabuleiros_lado_a_lado(tabuleiro_jogador, tabuleiro_computador)

# Quantidade de blocos por modelo de navio
CONFIGURACAO = {
    'destroyer': 3,
    'porta-avioes': 5,
    'submarino': 2,
    'torpedeiro': 3,
    'cruzador': 2,
    'couracado': 4
}

# Países e seus números
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

# Separação entre o tabuleiro e os países
print("----------------------------------------------------------------------------------------------------")

# Frotas de cada país
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

# Jogador vai escolher o seu país
def jogador_escolhe_pais():
    while True:
        for num, pais in PAISES.items():
            print(f'{num}: {pais}')
        escolha_numero_pais = int(input("Digite o número de nação que você irá defender: "))
        if escolha_numero_pais in PAISES:
            pais_escolhido = f"{escolha_numero_pais}: {PAISES[escolha_numero_pais]}"
            print(f"Você irá defender o país {PAISES[escolha_numero_pais]}")
            return pais_escolhido
        else:
            print("Nação desconhecida. Digite um número válido.")

# Computador escolhe um país diferente do jogador aleatoriamente e printa o país escolhido
def computador_escolhe_pais(pais_jogador):
    paises_disponiveis_comp = list(PAISES.values())
    pais_jogador_nome = pais_jogador.split(': ')[1]  # extrai apenas o nome do país usado pelo jogador

    escolha_do_pais_computador = random.choice(paises_disponiveis_comp)
    print(f'O computador escolheu o país {escolha_do_pais_computador}')
    for key, value in PAISES.items():
        if value == escolha_do_pais_computador:
            return f"{key}: {value}"

# Função do jogador para alocar barcos no tabuleiro na vertical ou horizontal.
def colocar_barcos_jogador(tabuleiro, frota_pais, configuracao):
    for navio, quantidade in frota_pais.items():
        for _ in range(quantidade):
            while True:
                print(f"Posicione o seu {navio} de tamanho {configuracao[navio]}")
                try:
                    linha_inicial = int(input("Escolha a linha inicial (1-10): ")) - 1
                except ValueError:
                    print("Local desejado não está participando da guerra. Digite um número válido.")
                    continue
                coluna_inicial = ord(input("Escolha a coluna inicial (A-J): ").upper()) - ord('A')
                orientacao = input("Escolha a orientação (horizontal/vertical): ").lower()
                if orientacao == 'h':
                    orientacao = 'horizontal'
                elif orientacao == 'v':
                    orientacao = 'vertical'

                if orientacao == 'horizontal' and coluna_inicial + configuracao[navio] <= 10:
                    if all(tabuleiro[linha_inicial][coluna_inicial+i] == ' ' for i in range(configuracao[navio])):
                        for i in range(configuracao[navio]):
                            tabuleiro[linha_inicial][coluna_inicial+i] = CORES['green'] + ' ' + CORES['reset']
                        break
                elif orientacao == 'vertical' and linha_inicial + configuracao[navio] <= 10:
                    if all(tabuleiro[linha_inicial+i][coluna_inicial] == ' ' for i in range(configuracao[navio])):
                        for i in range(configuracao[navio]):
                            tabuleiro[linha_inicial+i][coluna_inicial] = CORES['green'] + ' ' + CORES['reset']
                        break
                print("Posição inválida. Por favor, escolha novamente.")
            imprimir_tabuleiros_lado_a_lado(tabuleiro, tabuleiro_computador)  # imprime os tabuleiros após alocar cada barco

# Função que coloca os barcos do computador
def colocar_barcos_computador(tabuleiro, frota_pais, configuracao):
    for navio, quantidade in frota_pais.items():
        for _ in range(quantidade):
            while True:
                linha_inicial = random.randint(0, 9)
                coluna_inicial = random.randint(0, 9)
                orientacao = random.choice(['horizontal', 'vertical'])

                if orientacao == 'horizontal' and coluna_inicial + configuracao[navio] <= 10:
                    if all(tabuleiro[linha_inicial][coluna_inicial+i] == ' ' for i in range(configuracao[navio])):
                        for i in range(configuracao[navio]):
                            tabuleiro[linha_inicial][coluna_inicial+i] = 'O'
                        break
                elif orientacao == 'vertical' and linha_inicial + configuracao[navio] <= 10:
                    if all(tabuleiro[linha_inicial+i][coluna_inicial] == ' ' for i in range(configuracao[navio])):
                        for i in range(configuracao[navio]):
                            tabuleiro[linha_inicial+i][coluna_inicial] = 'O'
                        break

# Função para formatar as células do tabuleiro
def formatar_celula(celula):
    if celula == 'O':
        return CORES['green'] + ' ' + CORES['reset']
    elif celula == '{}'.format(CORES['red'], 'B', CORES['reset']):
        return CORES['red'] + 'B' + CORES['reset']
    elif celula == '{}'.format(CORES['blue'], 'A', CORES['reset']):
        return CORES['blue'] + 'A' + CORES['reset']
    else:
        return ' ' # adiciona um espaço extra para corresponder ao comprimento das outras células

# Função para o jogador atirar
# Função para o jogador atirar
def atirar(tabuleiro, linha, coluna):
    # Verifica se o local já foi atirado
    if tabuleiro[linha][coluna] in [CORES['red'] + '         B' + CORES['reset'], CORES['blue'] + '          A' + CORES['reset']]:
        print("Você já atirou aqui! Escolha outro lugar.")
        return False
    # Verifica se acertou um barco
    elif tabuleiro[linha][coluna] == 'O':
        tabuleiro[linha][coluna] = CORES['red'] + '         B' + CORES['reset']
        print(f"BOOOM! Você acertou na linha {linha+1}, coluna {chr(coluna+65)}")
        time.sleep(2)
        return True
    # Se atirou na água
    else:
        tabuleiro[linha][coluna] = CORES['blue'] + '         A' + CORES['reset']
        print(f"Água. Você atirou na linha {linha+1}, coluna {chr(coluna+65)}")
        time.sleep(2)
        return True

# Função para o computador atirar
# Função para o computador atirar
def atirar_aleatorio(tabuleiro):
    possiveis_coordenadas = [(linha, coluna) for linha in range(10) for coluna in range(10) if tabuleiro[linha][coluna] not in [CORES['red'] + 'B' + CORES['reset'], CORES['blue'] + 'A' + CORES['reset']]]
    while True:
        linha, coluna = random.choice(possiveis_coordenadas)
        if tabuleiro[linha][coluna] == ' ' or tabuleiro[linha][coluna] == CORES['green'] + ' ' + CORES['reset']:
            if tabuleiro[linha][coluna] == CORES['green'] + ' ' + CORES['reset']:
                tabuleiro[linha][coluna] = CORES['red'] + 'B' + CORES['reset']
                print(f"BOOOM! O computador acertou na linha {linha+1}, coluna {chr(coluna+65)}")
                time.sleep(2)
                return
            else:
                tabuleiro[linha][coluna] = CORES['blue'] + 'A' + CORES['reset']
                print(f"Água. O computador atirou na linha {linha+1}, coluna {chr(coluna+65)}")
                time.sleep(2)
                return


# Função para verificar se todos os barcos do computador foram atingidos
def verificar_barcos_computador(tabuleiro):
    for linha in tabuleiro:
        for celula in linha:
            if 'O' in celula:
                return False
    print("Você derrubou todos os barcos do Computador. Você venceu!")
    return True

# Função para verificar se todos os barcos do jogador foram atingidos
def verificar_barcos_jogador(tabuleiro):
    for linha in tabuleiro:
        if CORES['green'] + ' ' + CORES['reset'] in linha:
            return False
    print("O computador derrubou todos os seus barcos. Você perdeu!")
    return True

# Programa principal
if __name__ == "__main__":
    pais_jogador = jogador_escolhe_pais()
    pais_computador = computador_escolhe_pais(pais_jogador)
    colocar_barcos_jogador(tabuleiro_jogador, PAISES_FROTAS[pais_jogador], CONFIGURACAO)
    colocar_barcos_computador(tabuleiro_computador, PAISES_FROTAS[pais_computador], CONFIGURACAO)
    imprimir_tabuleiros_lado_a_lado(tabuleiro_jogador, tabuleiro_computador)
    print("Os barcos do seu oponente já estão em posição de batalha")
    time.sleep(3)
    print("Atenção, a batalha vai começar em 5 segundos!")
    time.sleep(1)
    print("5...")
    time.sleep(1)
    print("4...")
    time.sleep(1)
    print("3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(1)
    print("Vamos la!")
    time.sleep(1) 
    imprimir_tabuleiros_lado_a_lado(tabuleiro_jogador, tabuleiro_computador)
    while True:
        while True:
            try:
                linha = int(input("Escolha a linha para atirar (1-10): ")) - 1
                if linha < 0 or linha > 9:
                    print("Linha inválida. Por favor, escolha um número entre 1 e 10.")
                    continue
                break
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")
        while True:
            try:
                coluna = ord(input("Escolha a coluna para atirar (A-J): ").upper()) - ord('A')
                if coluna < 0 or coluna > 9:
                    print("Coluna inválida. Por favor, escolha uma letra entre A e J.")
                    continue
                break
            except TypeError:
                print("Entrada inválida. Por favor, digite uma letra.")
        if atirar(tabuleiro_computador, linha, coluna):
            if verificar_barcos_computador(tabuleiro_computador): 
                break
            atirar_aleatorio(tabuleiro_jogador)
            imprimir_tabuleiros_lado_a_lado(tabuleiro_jogador, tabuleiro_computador)
            if verificar_barcos_jogador(tabuleiro_jogador):
                break

