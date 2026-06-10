import random                                             # IMPORTA FUNÇÕES DE ALEATORIEDADE PARA BATALHAS, DROPS E DANO
import time                                               # IMPORTA PAUSAS USADAS NO TEXTO LENTO

# ======================================
#              TALES OF SG 
# ======================================
# PROJETO AVALIATIVO DE PYTHON
# KELLVYN - MENU, NAVEGAÇÃO E CADASTRO
# WALBER  - FUNÇÕES, ORGANIZAÇÃO E TESTES
# JOÃO    - LISTAS, VALIDAÇÕES E RELATÓRIO


# ======================================
# INVENTÁRIO DO JOGADOR
# RESPONSÁVEL: JOÃO
# LISTA DE ITENS INICIAIS
# ======================================

inventario = [
    "Poção SaBOUR Guaraná",
    "Poção SaBOUR Guaraná",  #POÇÕES INICIAIS PARA O JOGADOR NÃO FICAR NA MÃO LOGO DE CARA
    "Poção SaBOUR Guaraná"
]

# ======================================
# CORES DO TERMINAL 
# PRA DEIXAR TUDO MAIS BONITO
# ======================================

VERMELHO = "\033[91m" 
VERDE = "\033[92m"
AMARELO = "\033[93m"  #ISSO É AUTO EXPLICATIVO...
AZUL = "\033[94m"
ROXO = "\033[95m"
RESET = "\033[0m" #DEIXA A COR PADRÃO DO TERMINAL

# ======================================
# MAPAS COM OS INIMIGOS E BOSSES
# RESPONSÁVEL: JOÃO
# LISTAS E DICIONÁRIOS DO JOGO
# ======================================

mapa_atual = 0                                            # COMEÇA O JOGO NO PRIMEIRO MAPA DA LISTA

mapas = [                                                 # LISTA PRINCIPAL COM TODOS OS MAPAS DO JOGO
    {#MAPA DE SANTA LUZIA
        "nome": "Santa Luzia",
        "inimigos": [
            "Monge do Ponto Escuro",
            "Cavaleiro da Passagem Perdida",
            "Arauto da Luz Quebrada",
            "Fiscal das Carroças"
        ],
        "boss": "Bispo de Luzia",
        "derrotados": [],
        "boss_derrotado": False
    },
    
    {#MAPA DE JARDIM CATARINA
        "nome": "Jardim Catarina",
        "inimigos": [
            "Bruxo da Laje",
            "Rato do Valão Negro",
            "Arqueiro do Catarina",
            "Bárbaro da Rua de Terra"
        ],
        "boss": "Rei Catarina, o Caótico",
        "derrotados": [],
        "boss_derrotado": False
    },
    
    {#MAPA DE ALCÂNTARA
        "nome": "Alcântara",
        "inimigos": [
            "Cavaleiro do Terminal",
            "Mercador do Calçadão",
            "Sentinela da Passarela",
            "Ladrão das Vans Reais"
        ],
        "boss": "Lord Alcântarion",
        "derrotados": [],
        "boss_derrotado": False
    },
    
    {#MAPA DE CALIFÓRNIA
        "nome": "Califórnia",
        "inimigos": [
            "Condutor da Carruagem Errada",
            "Andarilho da Placa Apagada",
            "Arqueiro da Rua Sem Saída",
            "Cobrador do Retorno Impossível"
        ],
        "boss": "Barão da Califórnia",
        "derrotados": [],
        "boss_derrotado": False
    },
    
    {#MAPA DO CENTRO DE SÃO GONÇALO
        "nome": "Centro de São Gonçalo",
        "inimigos": [
            "Guardião da BR-101",
            "Cavaleiro da Guanabara",
            "Feiticeiro do Centro Antigo",
            "Arauto dos Sete Bairros"
        ],
        "boss": "Guardião do X-Tudo Lendário",
        "derrotados": [],
        "boss_derrotado": False
    }
]

# ======================================
# JOGADOR
# RESPONSÁVEL: WALBER
# STATUS E ATRIBUTOS DO PERSONAGEM
# ======================================

jogador = {                                               # DICIONÁRIO QUE GUARDA TODOS OS STATUS DO PERSONAGEM
    "nome": "",
    "classe": "",
    "vida": 100,
    "vida_max": 100,    #SAO OS STATS NORMAIS DO JOGADOR, MAS ELES VÃO MUDAR DEPENDENDO DA CLASSE ESCOLHIDA (ISSO SE O CODIGO ESTIVER FUNCIONANDO)
    "ataque": 15,
    "nivel": 1,
    "xp": 0,
    "grana": 50
}

# ======================================
# SISTEMA PARA DEIXAR O TEXTO LENTINHO LENTINHO
# RESPONSÁVEL: WALBER
# EFEITO DE NARRAÇÃO DO JOGO
# ======================================

def texto_lento(texto, velocidade=0.015):                 # FUNÇÃO QUE IMPRIME O TEXTO LETRA POR LETRA
    for letra in texto:                                   # PERCORRE CADA LETRA DO TEXTO RECEBIDO
        print(letra, end="", flush=True)                  # MOSTRA A LETRA SEM PULAR LINHA
        time.sleep(velocidade)                            # FAZ UMA PEQUENA PAUSA ENTRE AS LETRAS
    print()                                               # PULA UMA LINHA NO FINAL DO TEXTO

#ISSO É PARA DEIXAR IGUAL O INDICADOR DE ANVANÇAR TEXTO DO POKEMON
def esperar():                                            # PAUSA A HISTÓRIA ATÉ O JOGADOR APERTAR ENTER
    input("\nAperte ENTER ▼...")                          # ESPERA O JOGADOR AVANÇAR O TEXTO
    print("\033[F\033[K", end="")                         # LIMPA A LINHA ANTERIOR DO TERMINAL
    print("\033[F\033[K", end="")                         # LIMPA A LINHA ANTERIOR DO TERMINAL


def narrar(texto):                                        # JUNTA TEXTO LENTO COM PAUSA DE AVANÇO
    texto_lento(texto)                                    # MOSTRA A NARRAÇÃO COM EFEITO LENTO
    esperar()                                             # AGUARDA O JOGADOR ANTES DE CONTINUAR


# ======================================
# INTRODUÇÃO DA HISTÓRIA
# RESPONSÁVEL: KELLVYN
# APRESENTAÇÃO INICIAL DO JOGO
# ======================================

def introducao():                                         
    # MOSTRA A ABERTURA E O COMEÇO DA HISTÓRIA
    print(VERDE)                                          # TROCA A COR DO TERMINAL PARA VERDE
    print(r"""
 _________  ________  ___       _______   ________              ________  ________         ________  ________     
|\___   ___\\   __  \|\  \     |\  ___ \ |\   ____\            |\   __  \|\  _____\       |\   ____\|\   ____\    
\|___ \  \_\ \  \|\  \ \  \    \ \   __/|\ \  \___|_           \ \  \|\  \ \  \__/        \ \  \___|\ \  \___|    
     \ \  \ \ \   __  \ \  \    \ \  \_|/_\ \_____  \           \ \  \\\  \ \   __\        \ \_____  \ \  \  ___  
      \ \  \ \ \  \ \  \ \  \____\ \  \_|\ \|____|\  \           \ \  \\\  \ \  \_|         \|____|\  \ \  \|\  \ 
       \ \__\ \ \__\ \__\ \_______\ \_______\____\_\  \           \ \_______\ \__\            ____\_\  \ \_______\
        \|__|  \|__|\|__|\|_______|\|_______|\_________\           \|_______|\|__|           |\_________\|_______|
                                            \|_________|                                     \|_________|                                                                                                 
                                                                        
""")
    print(VERDE)                                          # TROCA A COR DO TERMINAL PARA VERDE
    print("Uma história de:")
    print("Walber, João e Kellvyn.")

 
    
    print(AMARELO)                                        # TROCA A COR DO TERMINAL PARA AMARELO
    print("")                                             # DEIXA UMA LINHA EM BRANCO PARA ORGANIZAR A TELA
    narrar("Esta história começa em Santa Luzia.")
    narrar("Não por causa de uma guerra, de uma profecia ou de um dragão.")
    narrar("Começa porque alguém ouviu falar de um X-Tudo lendário no Centro de São Gonçalo.")
    narrar("Um lanche comentado em voz baixa por viajantes, entregadores e senhores sentados na praça.")
    narrar("Dizem que ele sustenta um homem por dias.")
    narrar("Dizem também que isso é exagero.")
    narrar("Mas ninguém discute uma coisa: o lanche existe.")
    narrar("E o nosso viajante estava com fome.")
    print("")                                             # DEIXA UMA LINHA EM BRANCO PARA ORGANIZAR A TELA


# ======================================
# HISTÓRIA DOS MAPAS
# RESPONSÁVEL: KELLVYN
# NARRAÇÃO DA PROGRESSÃO
# ======================================

def historia_mapa():                                      # MOSTRA A HISTÓRIA DE ACORDO COM O MAPA ATUAL
    mapa = mapas[mapa_atual]["nome"]                      # PEGA O NOME DO MAPA ONDE O JOGADOR ESTÁ

    #ISSO É PARA CONTAR A HISTORIA DE CADA MAPA QUANDO O JOGADOR CHEGAR NELE

    if mapa == "Santa Luzia":                             # HISTÓRIA EXIBIDA NO PRIMEIRO MAPA
        print(AMARELO)                                    # TROCA A COR DO TERMINAL PARA AMARELO
        narrar("Santa Luzia era conhecida por suas tavernas e vendedores ambulantes.")
        narrar("O cheiro de carne assada dominava as ruas durante boa parte do dia.")
        narrar("Mesmo assim, o viajante não parou em nenhuma delas.")
        narrar("Seu objetivo era outro.")
        narrar("No Centro de São Gonçalo, dizia a lenda, era servido o X-Tudo Supremo.")
        narrar("E nada que existisse em Santa Luzia parecia capaz de competir com essa promessa.")
        narrar("Com isso em mente, ele iniciou sua jornada.")
        narrar("No papel, a viagem parecia simples.")
        narrar("Mas o papel nunca pegou uma carruagem lotada em horário ruim.")


    elif mapa == "Jardim Catarina":                       # HISTÓRIA EXIBIDA NO SEGUNDO MAPA
        print(AMARELO)                                    # TROCA A COR DO TERMINAL PARA AMARELO
        narrar("Após deixar Santa Luzia para trás, o viajante chegou ao Jardim Catarina.")
        narrar("Dizem que ninguém entra aqui sem ouvir pelo menos três histórias diferentes sobre o mesmo lugar.")
        narrar("Alguns afirmam que o bairro é amaldiçoado.")
        narrar("Outros dizem que isso é exagero.")
        narrar("Mas todos concordam em uma coisa:")
        narrar("É melhor prestar atenção por onde anda.")
        narrar("Os moradores observam tudo atrás de portões antigos.")
        narrar("E figuras estranhas costumam aparecer para quem está viajando sozinho.")
        narrar("Ainda assim, o lendário X-Tudo Supremo está cada vez mais próximo.")
        narrar("Voltar agora seria covardia.")


    elif mapa == "Alcântara":                             # HISTÓRIA EXIBIDA NO TERCEIRO MAPA
        print(AMARELO)                                    # TROCA A COR DO TERMINAL PARA AMARELO
        narrar("O viajante chega a Alcântara, o grande centro comercial da região.")
        narrar("Mercadores anunciam ofertas, carruagens disputam espaço e todo mundo parece estar atrasado para alguma coisa.")
        narrar("Por um breve momento, ele até esqueceu do X-Tudo Supremo.")
        narrar("Apenas por um breve momento.")
        narrar("Entre lojas, tavernas e vendedores insistentes, era possível encontrar praticamente qualquer coisa.")
        narrar("Desde uma simples poção até equipamentos capazes de salvar uma jornada.")
        narrar("Ou acabar com ela.")
        narrar("Alguns itens pareciam falsificados.")
        narrar("Outros provavelmente pertenciam a outra pessoa poucas horas antes de serem colocados à venda.")
        narrar("Ainda assim, talvez fosse melhor aproveitar a oportunidade.")
        narrar("Ninguém sabe o que espera um aventureiro depois de Alcântara.")


    elif mapa == "Califórnia":                            # HISTÓRIA EXIBIDA NO QUARTO MAPA
        print(AMARELO)                                    # TROCA A COR DO TERMINAL PARA AMARELO
        narrar("Após sair de Alcântara, o viajante embarca em uma carruagem rumo ao Centro.")
        narrar("Pelo menos era isso que ele achava.")
        narrar("Alguns minutos depois, percebe que a placa estava errada, ou talvez ele só não tenha lido direito.")
        narrar("Assim, por erro, destino ou pura falta de atenção, ele chega ao Jardim Califórnia.")
        narrar("Comparado ao caos de Alcântara, o lugar parecia muito mais tranquilo.")
        narrar("As ruas eram desertas mas havia uma sensação de perigo como se alguém estivesse observando.")
        narrar("Algumas figuras observavam de longe.")
        narrar("Nenhuma delas parecia interessada em conversar.")
        narrar("Mas a lembrança do lendário X-Tudo Supremo lhe encheu de determinação.")
        narrar("Agora ele precisava encontrar o caminho correto.")
        narrar("E torcer para não pegar a carruagem errada uma segunda vez.")


    elif mapa == "Centro de São Gonçalo":                 # HISTÓRIA EXIBIDA NO MAPA FINAL
        print(AMARELO)                                    # TROCA A COR DO TERMINAL PARA AMARELO
        narrar("Depois de tanto desvio, poeira e humilhação pública, o Centro finalmente aparece.")
        narrar("O cheiro de chapa quente atravessa as ruas como um chamado divino.")
        narrar("O X-Tudo lendário está perto.")
        narrar("Mas nenhuma lenda é entregue sem teste final.")


# ======================================
# CRIAÇÃO DE PERSONAGEM
# RESPONSÁVEL: KELLVYN
# CADASTRO E ESCOLHA DE CLASSE
# ======================================

def criar_personagem():                                   # CUIDA DA CRIAÇÃO DO PERSONAGEM DO JOGADOR
    nome = input("Qual é seu vulgo?: ").strip()           # PEDE O NOME E REMOVE ESPAÇOS SOBRANDO

    if nome == "":                                        # VERIFICA SE O JOGADOR DEIXOU O NOME VAZIO
        return criar_personagem()  # CHAMADA RECURSIVA PARA GARANTIR QUE O JOGADOR ESCOLHA UM NOME VÁLIDO
    

    jogador["nome"] = nome                                # SALVA O NOME ESCOLHIDO NO DICIONÁRIO DO JOGADOR

    print("\n===== ESCOLHA SUA CLASSE =====")
    print("1 - Mago")
    print("2 - Bárbaro")
    print(f"3 - Arqueiro") #OPÇÃO DE CLASSE COM STATUS SUPER FORTES PARA FACILITAR O JOGO PARA QUEM QUISER APENAS CURTIR A HISTÓRIA SEM SE PREOCUPAR COM DIFICULDADE
    print("\nCada classe tem seus próprios atributos de vida e ataque, além de habilidades especiais. Escolha sabiamente!")
    print("")                                             # DEIXA UMA LINHA EM BRANCO PARA ORGANIZAR A TELA

    while True:                                           # REPETE ATÉ O JOGADOR ESCOLHER UMA OPÇÃO VÁLIDA
        classe = input("Escolha: ")                       # RECEBE A CLASSE ESCOLHIDA PELO JOGADOR
        if classe in ["1", "2", "3"]:                     # CONFERE SE A CLASSE EXISTE NO MENU
            break                                         # SAI DO LAÇO QUANDO A ESCOLHA É VÁLIDA
        print("Opção inválida. Escolha novamente.")       # AVISA QUE A ESCOLHA NÃO EXISTE

    if classe == "1":                                     # CONFIGURA OS ATRIBUTOS DO MAGO
        jogador["classe"] = "Mago"                        # DEFINE A CLASSE COMO MAGO
        jogador["vida"] = 80
        jogador["vida_max"] = 80
        jogador["ataque"] = 25

    elif classe == "2":                                   # CONFIGURA OS ATRIBUTOS DO BÁRBARO
        jogador["classe"] = "Bárbaro"                     # DEFINE A CLASSE COMO BÁRBARO
        jogador["vida"] = 130
        jogador["vida_max"] = 130
        jogador["ataque"] = 18

    elif classe == "3":                                   # CONFIGURA OS ATRIBUTOS DO ARQUEIRO
        jogador["classe"] = "Arqueiro"                    # DEFINE A CLASSE COMO ARQUEIRO
        jogador["vida"] = 100
        jogador["vida_max"] = 100
        jogador["ataque"] = 20
        

    narrar(f"{jogador['nome']} entrou para a história de São Gonçalo.")
    print("")                                             # DEIXA UMA LINHA EM BRANCO PARA ORGANIZAR A TELA
    narrar(f"Classe escolhida: {jogador['classe']}.")
    print("")                                             # DEIXA UMA LINHA EM BRANCO PARA ORGANIZAR A TELA


# ======================================
# ORGANIZAÇÃO DOS STATUS
# RESPONSÁVEL: WALBER
# EXIBIÇÃO DOS ATRIBUTOS
# ======================================

def mostrar_status():                                     # MOSTRA OS DADOS ATUAIS DO JOGADOR
    mapa = mapas[mapa_atual]                              # PEGA O DICIONÁRIO COMPLETO DO MAPA ATUAL

    print(f"\n{AZUL}===== STATUS ====={RESET}")
    print(f"nome: {jogador['nome']}")                     # MOSTRA O NOME DO JOGADOR
    print(f"Classe: {jogador['classe']}")                 # MOSTRA A CLASSE ESCOLHIDA
    print(f"Mapa atual: {mapa['nome']}")                  # MOSTRA ONDE O JOGADOR ESTÁ
    print(f"Vida: {jogador['vida']}/{jogador['vida_max']}")  # MOSTRA VIDA ATUAL E VIDA MÁXIMA
    print(f"Ataque: {jogador['ataque']}")                 # MOSTRA O ATAQUE ATUAL
    print(f"Nível: {jogador['nivel']}")                   # MOSTRA O NÍVEL ATUAL
    print(f"XP: {jogador['xp']}/50")                      # MOSTRA O PROGRESSO ATÉ UPAR
    print(f"Grana: {jogador['grana']}")                   # MOSTRA O DINHEIRO DO JOGADOR
    print(f"Inimigos derrotados: {len(mapa['derrotados'])}/{len(mapa['inimigos'])}")
    print(f"Boss derrotado: {mapa['boss_derrotado']}")


# ======================================
# MENU PARA MOSTRAR O MAPA
# RESPONSÁVEL: KELLVYN
# NAVEGAÇÃO VISUAL
# ======================================

def mostrar_mapa():                                       # MOSTRA TODOS OS MAPAS E DESTACA O ATUAL
    print(f"\n{ROXO}===== MAPA ====={RESET}")

    for i, mapa in enumerate(mapas):                      # PERCORRE OS MAPAS COM ÍNDICE E CONTEÚDO
        if i == mapa_atual:                               # VERIFICA SE ESTE É O MAPA ATUAL
            print(f">>> {mapa['nome']} <<<")
        else:                                             # CASO NÃO SEJA O MAPA ATUAL
            print(mapa["nome"])


# ======================================
# SISTEMA DE UPAR DE NÍVEL
# RESPONSÁVEL: WALBER
# PROGRESSÃO DO JOGADOR
# ======================================

def subir_nivel():                                        # VERIFICA SE O JOGADOR DEVE SUBIR DE NÍVEL
    while jogador["xp"] >= 50:                            # CONTINUA UPANDO ENQUANTO HOUVER XP SUFICIENTE
        jogador["nivel"] += 1                             # AUMENTA O NÍVEL EM 1
        jogador["ataque"] += 5                            # AUMENTA O ATAQUE AO SUBIR DE NÍVEL
        jogador["xp"] -= 50                               # GASTA 50 DE XP PARA CADA NÍVEL

        print(f"\n{VERDE}===== LEVEL UP ====={RESET}")
        print(f"Agora você é nível {jogador['nivel']}!")
        print("Ataque aumentado em +5!")


# ======================================
# REMEDIO GENÉRICO (POÇÃO)
# RESPONSÁVEL: WALBER
# CURA DO JOGADOR
# POÇÃO SABOUR GUARANÁ: SE CUROU, A GENTE NÃO QUESTIONA
# ======================================

def usar_pocao():                                         # USA UMA POÇÃO DO INVENTÁRIO PARA CURAR VIDA
    if "Poção SaBOUR Guaraná" in inventario:                    # CONFERE SE EXISTE POÇÃO NO INVENTÁRIO
        jogador["vida"] += 40                             # CURA 40 PONTOS DE VIDA

        if jogador["vida"] > jogador["vida_max"]:         # IMPEDE A VIDA DE PASSAR DO MÁXIMO
            jogador["vida"] = jogador["vida_max"]         # RESTAURA A VIDA AO MÁXIMO

        inventario.remove("Poção SaBOUR Guaraná")               # REMOVE UMA POÇÃO DEPOIS DE USAR

        print(f"\n{VERDE}Poção SaBOUR Guaraná usada!{RESET}")
        print(f"Vida atual: {jogador['vida']}/{jogador['vida_max']}")

    else:                                                 # CASO NÃO TENHA POÇÃO NO INVENTÁRIO
        print("\nVocê não possui Poção SaBOUR Guaraná.")


# ======================================
# ATAQUE DO INIMIGO E ESQUIVA AUTOMATICA
# RESPONSÁVEL: WALBER
# DANO E CHANCE DE DESVIO
# ======================================

def ataque_do_inimigo(inimigo, ataque_inimigo):           # CONTROLA O ATAQUE E A CHANCE DE ESQUIVA DO INIMIGO
    esquivou = False                                      # COMEÇA ASSUMINDO QUE O JOGADOR NÃO ESQUIVOU

    if jogador["classe"] == "Arqueiro":                   # ARQUEIRO TEM CHANCE MAIOR DE ESQUIVAR
        if random.randint(1, 100) <= 30:                  # SORTEIA 30% DE CHANCE DE ESQUIVA
            esquivou = True      
    else:                                                 # CASO NÃO SEJA O MAPA ATUAL
        if random.randint(1, 100) <= 10:                  # OUTRAS CLASSES TÊM 10% DE ESQUIVA
            esquivou = True       
            
    if jogador ["classe"] == "Arqueiro" and esquivou:
            print(f"\n{AZUL}ESQUIVO, ESQUIVO!{RESET}")        # MARCA QUE O JOGADOR ESQUIVOU
            
    elif esquivou:                                          # SE A ESQUIVA ACONTECEU
        print(f"\n{AMARELO}Você desviou!{RESET}")
   
    else:                                                 # CASO NÃO ESQUIVOU, O INIMIGO ACERTA O ATAQUE
        dano_inimigo = ataque_inimigo + random.randint(1, 5)  # CALCULA DANO DO INIMIGO COM VARIAÇÃO ALEATÓRIA
        jogador["vida"] -= dano_inimigo                   # TIRA VIDA DO JOGADOR

        if jogador["vida"] < 0:                           # EVITA VIDA NEGATIVA
            jogador["vida"] = 0                           # DEFINE VIDA COMO ZERO NO MÍNIMO

        print(f"O {inimigo} atacou e causou {dano_inimigo} de dano!")


# ======================================
# SISTEMA DE BATALHA
# RESPONSÁVEL: WALBER
# COMBATE, DANO, XP E VITÓRIA
# ======================================

def batalha(boss=False):                                  # INICIA UMA BATALHA COMUM OU CONTRA BOSS
    mapa = mapas[mapa_atual]                              # PEGA O DICIONÁRIO COMPLETO DO MAPA ATUAL

    inimigos_restantes = []                               # LISTA QUE RECEBERÁ INIMIGOS AINDA VIVOS

    for inimigo in mapa["inimigos"]:                      # PERCORRE OS INIMIGOS DO MAPA ATUAL
        if inimigo not in mapa["derrotados"]:             # VERIFICA SE O INIMIGO AINDA NÃO FOI VENCIDO
            inimigos_restantes.append(inimigo)            # ADICIONA O INIMIGO NA LISTA DE RESTANTES

    if boss:                                              # RECOMPENSAS ESPECIAIS PARA BOSS
        if len(inimigos_restantes) > 0:                   # BLOQUEIA BOSS SE AINDA TIVER INIMIGOS COMUNS
            print("\nVocê precisa derrotar todos os inimigos comuns antes do boss.")
            return                                        # ENCERRA A FUNÇÃO E VOLTA AO MENU

        if mapa["boss_derrotado"]:                        # IMPEDE REPETIR BOSS JÁ DERROTADO
            print("\nEsse boss já foi derrotado.")
            return                                        # ENCERRA A FUNÇÃO E VOLTA AO MENU

        inimigo = mapa["boss"]                            # DEFINE O INIMIGO COMO O BOSS DO MAPA
        vida_inimigo = random.randint(110, 150)           # SORTEIA A VIDA DO BOSS
        ataque_inimigo = random.randint(25, 35)  
        
        if mapa["nome"] == "Centro de São Gonçalo":   
            vida_inimigo = random.randint(180, 230)
            ataque_inimigo = random.randint(30, 45)
        else:
            vida_inimigo = random.randint(110, 150)
            ataque_inimigo = random.randint(25, 35)# SORTEIA O ATAQUE DO BOSS

        print(f"\n{VERMELHO}===== BOSS DE {mapa['nome'].upper()} ====={RESET}")

    else:                                                 # CASO SEJA UMA BATALHA COM INIMIGO COMUM
        if len(inimigos_restantes) == 0:                  # VERIFICA SE JÁ ACABARAM OS INIMIGOS COMUNS
            print("\nTodos os inimigos comuns desse mapa já foram derrotados.")
            print("Agora você pode enfrentar o boss.")
            return                                        # ENCERRA A FUNÇÃO E VOLTA AO MENU

        inimigo = inimigos_restantes[0]                   # PEGA O PRÓXIMO INIMIGO COMUM DA LISTA
        vida_inimigo = random.randint(55, 70)             # SORTEIA A VIDA DO INIMIGO COMUM
        ataque_inimigo = random.randint(12, 20)           # SORTEIA O ATAQUE DO INIMIGO COMUM

    narrar(f"{inimigo} apareceu em {mapa['nome']}!")

    while vida_inimigo > 0 and jogador["vida"] > 0:       # MANTÉM A BATALHA ENQUANTO OS DOIS ESTIVEREM VIVOS
        print(f"\n{AMARELO}Vida do {inimigo}: {vida_inimigo}{RESET}")
        print(f"{VERDE}Sua vida: {jogador['vida']}/{jogador['vida_max']}{RESET}")

        print("\n1 - Atacar")
        print("2 - Tomar poção")
        print("3 - Vazar")

        # ======================================
        # TRATAMENTO DE ERROS + VARIAVEIS DE CLASSE
        # RESPONSÁVEL: JOÃO
        # ======================================
        # O JOGO FOI FEITO PARA ENFRENTAR MONSTROS.
        # NÃO PARA ENFRENTAR QUEM DIGITA "ABUBEBLE" NO LUGAR DE "1" PARA ATACAR.
        # ======================================

        try:
            escolha = int(input("Escolha: "))             # LÊ A ESCOLHA DE BATALHA COMO NÚMERO INTEIRO
        except ValueError:                                # CAPTURA ERRO CASO DIGITEM TEXTO NO LUGAR DE NÚMERO
            print("\nOpção inválida.")
            continue                                      # VOLTA PARA O COMEÇO DO TURNO

# ======================================
# SISTEMA DE BATALHA
# RESPONSÁVEL: WALBER
# COMBATE, DANO, XP E VITÓRIA
# ======================================

        if escolha == 1:                                  # OPÇÃO DE ATACAR O INIMIGO
            dano = jogador["ataque"] + random.randint(1, 10)  # CALCULA DANO DO JOGADOR COM VARIAÇÃO ALEATÓRIA

            if jogador["classe"] == "Mago":
                if random.randint(1, 100) <= 25:          # SORTEIA 25% DE CHANCE DE MAGIA CRÍTICA
                    dano += 15                            # ADICIONA DANO EXTRA DO CRÍTICO MÁGICO
                    print(f"\n{ROXO}Criou alucinações com a ex. Enquanto o inimigo chora, ataque outra vez!{RESET}")

            elif jogador["classe"] == "Bárbaro":
                dano_extra = random.randint(3, 8)         # SORTEIA DANO EXTRA DO BÁRBARO
                dano += dano_extra                        # SOMA O DANO EXTRA AO ATAQUE FINAL
                print(f"\nAplicou um chute nos paises baixos! Dano Crítico!: {dano_extra}")

            vida_inimigo -= dano                          # REDUZ A VIDA DO INIMIGO

            if vida_inimigo < 0:                          # IMPEDE VIDA NEGATIVA DO INIMIGO
                vida_inimigo = 0                          # DEIXA A VIDA DO INIMIGO NO MÍNIMO ZERO

            print(f"\nVocê causou {dano} de dano!")

            if vida_inimigo > 0:                          # INIMIGO SÓ CONTRA-ATACA SE SOBREVIVER
                ataque_do_inimigo(inimigo, ataque_inimigo)  # EXECUTA O ATAQUE DO INIMIGO

        elif escolha == 2:                                # OPÇÃO DE USAR POÇÃO DURANTE A BATALHA
            vida_antes = jogador["vida"]                  # GUARDA A VIDA ANTES DE TENTAR USAR POÇÃO
            usar_pocao()                                  # CHAMA A FUNÇÃO DE CURA

            if jogador["vida"] > vida_antes and vida_inimigo > 0:  # INIMIGO ATACA SE A POÇÃO REALMENTE CUROU
                ataque_do_inimigo(inimigo, ataque_inimigo)  # EXECUTA O ATAQUE DO INIMIGO

        elif escolha == 3:                                # OPÇÃO DE FUGIR DA BATALHA
            print("\nTu meteu marcha!")
            return                                        # ENCERRA A FUNÇÃO E VOLTA AO MENU

        else:                                             # CASO O JOGADOR DIGITE UM NÚMERO QUE NÃO CORRESPONDE A NENHUMA OPÇÃO
            print("\nOpção inválida.")

    if jogador["vida"] > 0:                               # VERIFICA SE O JOGADOR VENCEU A BATALHA
        narrar(f"Você derrotou {inimigo}!")

        if boss:                                          # RECOMPENSAS ESPECIAIS PARA BOSS
            mapa["boss_derrotado"] = True                 # MARCA O BOSS COMO DERROTADO
            xp_ganho = random.randint(40, 70)             # SORTEIA XP MAIOR PARA BOSS
            print(f"\n{VERDE}Boss de {mapa['nome']} derrotado!{RESET}")
            dropar_item(boss=True)                        # GERA RECOMPENSA DE BOSS
        else:                                             # CASO NÃO SEJA O MAPA ATUAL
            mapa["derrotados"].append(inimigo)            # SALVA O INIMIGO COMUM COMO DERROTADO
            xp_ganho = random.randint(10, 30)             # SORTEIA XP DE INIMIGO COMUM
            dropar_item()                                 # GERA RECOMPENSA DE INIMIGO COMUM

        jogador["xp"] += xp_ganho                         # ADICIONA XP AO JOGADOR

        print(f"XP ganho: {xp_ganho}")

        subir_nivel()                                     # CONFERE SE O XP FOI SUFICIENTE PARA UPAR

    else:                                                 # CASO O JOGADOR TENHA SIDO DERROTADO
        print(f"\n{VERMELHO}Tu foi de vala...{RESET}")
        jogador["vida"] = jogador["vida_max"]             # RESTAURA A VIDA AO MÁXIMO
        print("Você acordou alguns minutos depois.")
        print("Por sorte, o inimigo já tinha ido embora.")
        print("Sua vida foi restaurada.")
        return                                            # ENCERRA A FUNÇÃO E VOLTA AO MENU


# ======================================
# SISTEMA DE PROGRESSÃO DE NARRATIVA (IR PARA OUTRO MAPA)
# RESPONSÁVEL: KELLVYN
# AVANÇO ENTRE MAPAS
# ======================================

def avancar_mapa():                                       # TENTA LEVAR O JOGADOR PARA O PRÓXIMO MAPA
    global mapa_atual                                     # PERMITE ALTERAR A VARIÁVEL GLOBAL DO MAPA ATUAL

    mapa = mapas[mapa_atual]                              # PEGA O DICIONÁRIO COMPLETO DO MAPA ATUAL

    if not mapa["boss_derrotado"]:                        # SÓ LIBERA AVANÇO DEPOIS DE DERROTAR O BOSS
        print("\nVocê precisa derrotar o boss desse mapa antes de avançar.")
        return                                            # ENCERRA A FUNÇÃO E VOLTA AO MENU

    if mapa_atual < len(mapas) - 1:                       # VERIFICA SE AINDA EXISTE PRÓXIMO MAPA
        mapa_atual += 1                                   # AVANÇA PARA O PRÓXIMO MAPA DA LISTA
        jogador["vida"] = jogador["vida_max"]             # RESTAURA A VIDA AO MÁXIMO

        narrar(f"Você avançou para {mapas[mapa_atual]['nome']}!")
        narrar("Sua vida foi restaurada.")

        historia_mapa()                                   # MOSTRA A HISTÓRIA DO NOVO MAPA

    else:                                                 # CASO O JOGADOR ESTEJA NO ÚLTIMO MAPA E TENTE AVANÇAR
        print(f"\n{VERDE}===== FIM DE JOGO ====={RESET}")
        print("Você finalmente comeu o X-Tudo lendário.")
        print("São Gonçalo continua igual, mas pelo menos você não está mais com fome.")
        print("Só é uma pena para o vaso sanitário depois de ter comido aquilo...")


# ======================================
# SISTEMA DE DROPAR ITENS E GRANA APÓS BATALHAS
# RESPONSÁVEL: WALBER
# RECOMPENSAS APÓS BATALHAS
# ======================================
# DESCOBRIMOS QUE ACHAR UMA ESPADA NO CHÃO A CADA 30 SEGUNDOS
# NÃO ERA MUITO REALISTA.
# AGORA OS ITENS CAEM DOS INIMIGOS, QUE TAMBÉM NÃO É MUITO
# REALISTA, MAS PELO MENOS FAZ MAIS SENTIDO.
# ======================================

def dropar_item(boss=False):                              # GERA DINHEIRO E ITEM DEPOIS DA VITÓRIA
    chance = random.randint(1, 100)                     # SORTEIA A CHANCE DE DROPAR ITEM (BOSS TEM CHANCE DE 100%)

    if boss:                                              # RECOMPENSAS ESPECIAIS PARA BOSS
        grana_ganho = random.randint(35, 55)              # SORTEIA MAIS DINHEIRO PARA BOSS
    else:                                                 # CASO NÃO SEJA O MAPA ATUAL
        grana_ganho = random.randint(12, 22)              # SORTEIA DINHEIRO DE INIMIGO COMUM

    jogador["grana"] += grana_ganho                       # ADICIONA DINHEIRO AO JOGADOR
    print(f"Grana recebida: {grana_ganho}")

    if chance <= 30:                                     # DEIXA COM 30% DE CHANCE DE DROPAR UM ITEM
        item = random.choice([                            # SORTEIA QUAL ITEM SERÁ RECEBIDO
            "Poção SaBOUR Guaraná",
            "Escudo de Porta de Van",
            "Adaga Cega da Feirinha"
        ])

        inventario.append(item)                           # COLOCA O ITEM NO INVENTÁRIO
        print(f"Item dropado: {item}")

        if item == "Escudo de Porta de Van":              # APLICA BÔNUS SE O ITEM FOR ESCUDO
            jogador["vida_max"] += 5                      # AUMENTA A VIDA MÁXIMA PELO ESCUDO
            jogador["vida"] += 5                          # TAMBÉM CURA 5 PONTOS AO EQUIPAR O ESCUDO
            print("Vida máxima aumentada em +5!")
            
        elif item == "Adaga Cega da Feirinha":            # APLICA BÔNUS SE O ITEM FOR ADAGA
            jogador["ataque"] += 2                      # AUMENTA O ATAQUE PELA ADAGA
            print("Ataque aumentado em +2!")



# ======================================
# SISTEMA ANTI-KAUA
# RESPONSÁVEL: WALBER
# LIMITA STATUS ABSURDOS CASO ALGUÉM TENTE VIRAR O DONO DA GUANABARA NO LEVEL 1
# ======================================
# SE O JOGADOR FICAR FORTE DEMAIS ACIMA DO ESPERADO,
# O FISCAL REAL DO BALANCEAMENTO APARECE PARA CONFISCAR O EXCESSO.
# NÃO É ROUBO, É AJUSTE DE ROTEIRO.
# ======================================

def verificar_trapaca():                                  # VERIFICA SE O JOGADOR ESTÁ FORTE DEMAIS
    limite_ataque = 100                                   # ATAQUE MÁXIMO ESPERADO PARA UM JOGADOR COMUM
    limite_vida_max = 240                                 # VIDA MÁXIMA ESPERADA PARA UM JOGADOR COMUM
    limite_grana = 500                                    # DINHEIRO MÁXIMO ANTES DE PARECER ESQUEMA
    limite_itens = 20                                     # LIMITE DE ITENS PARA NÃO VIRAR UM MERCADO AMBULANTE

    trapaca_detectada = False                             # COMEÇA ASSUMINDO QUE ESTÁ TUDO NORMAL

    if jogador["ataque"] > limite_ataque:                 # VERIFICA SE O ATAQUE PASSOU DO LIMITE
        trapaca_detectada = True

    if jogador["vida_max"] > limite_vida_max:             # VERIFICA SE A VIDA MÁXIMA PASSOU DO LIMITE
        trapaca_detectada = True

    if jogador["grana"] > limite_grana:                   # VERIFICA SE A GRANA PASSOU DO LIMITE
        trapaca_detectada = True

    if len(inventario) > limite_itens:                    # VERIFICA SE TEM ITENS DEMAIS
        trapaca_detectada = True

    if trapaca_detectada:                                 # SE ALGO ESTIVER ABSURDO, O FISCAL APARECE
        print(f"\n{VERMELHO}===== COBRADOR DE IMPOSTOS STATAIS ====={RESET}")
        narrar("Uma presença estranha surge no caminho do viajante.")
        narrar("Um homem com um sorriso malandro apareceu em sua frente.")
        narrar("'Meu rapaz, que status são esses? está querendo quebrar a lógica do país?' ele pergunta.")
        narrar("'Infelizmente para você a cobrança de impostos statais será aplicada. Vamos dar uma olhada no que você tem aí...'")

        if jogador["ataque"] > limite_ataque:             # REDUZ O ATAQUE PARA O LIMITE ESPERADO
            ataque_roubado = jogador["ataque"] - limite_ataque
            jogador["ataque"] = limite_ataque
            print(f"Ataque confiscado: {ataque_roubado}")

        if jogador["vida_max"] > limite_vida_max:         # REDUZ A VIDA MÁXIMA PARA O LIMITE ESPERADO
            vida_roubada = jogador["vida_max"] - limite_vida_max
            jogador["vida_max"] = limite_vida_max

            if jogador["vida"] > jogador["vida_max"]:     # AJUSTA A VIDA ATUAL PARA NÃO PASSAR DO MÁXIMO
                jogador["vida"] = jogador["vida_max"]

            print(f"Vida máxima confiscada: {vida_roubada}")

        if jogador["grana"] > limite_grana:               # REMOVE O DINHEIRO ACIMA DO LIMITE
            grana_roubada = jogador["grana"] - limite_grana
            jogador["grana"] = limite_grana
            print(f"Grana confiscada: {grana_roubada}")

        if len(inventario) > limite_itens:                # REMOVE ITENS ACIMA DO LIMITE
            quantidade_roubada = len(inventario) - limite_itens
            del inventario[limite_itens:]
            print(f"Itens confiscados: {quantidade_roubada}")

        narrar("Após o confisco, o Cobrador de Impostos Statais desapareceu.")
        narrar("O viajante continuou forte, só não forte demais pois iria 'acabar com a lógica do país'.")


# ======================================
# INVENTÁRIO DO JOGADOR
# RESPONSÁVEL: KELLVYN
# MENU DE ITENS DO JOGADOR
# ======================================

def mostrar_inventario():                                 # MOSTRA OS ITENS QUE O JOGADOR POSSUI
    print(f"\n{AZUL}===== INVENTÁRIO ====={RESET}")

    if len(inventario) == 0:                              # VERIFICA SE A MOCHILA ESTÁ VAZIA
        print("Mochila vazia.")
        return                                            # ENCERRA A FUNÇÃO E VOLTA AO MENU

    for item in inventario:                               # PERCORRE CADA ITEM DO INVENTÁRIO
        print("-", item)

    print("\n1 - Usar Poção SaBOUR Guaraná\n")
    print("2 - Voltar")

    escolha = input("Escolha: ")                          # RECEBE A OPÇÃO ESCOLHIDA NO MENU

    if escolha == "1":                                    # ABRE UMA BATALHA COMUM
        usar_pocao()                                      # CHAMA A FUNÇÃO DE CURA
    elif escolha == "2":                                  # TENTA ENFRENTAR O BOSS
        print("\nVoltando...")
    else:                                                 # CASO NÃO SEJA O MAPA ATUAL
        print("\nOpção inválida.")


# ======================================
# LOJA EM ALCANTARA
# RESPONSÁVEL: KELLVYN
# COMPRA DE ITENS E EQUIPAMENTOS
# ======================================

def loja():                                               # ABRE O SISTEMA DA LOJA DE ALCÂNTARA
    mapa = mapas[mapa_atual]                              # PEGA O DICIONÁRIO COMPLETO DO MAPA ATUAL

    if mapa["nome"] != "Alcântara":                       # LOJA SÓ FUNCIONA NO MAPA ALCÂNTARA
        print("\nA loja fica em Alcântara. Vá até lá primeiro.")
        return                                            # ENCERRA A FUNÇÃO E VOLTA AO MENU

    if len(mapa["derrotados"]) < len(mapa["inimigos"]):   # LOJA ABRE SÓ DEPOIS DOS INIMIGOS SEREM DERROTADOS
        print("\nA loja ainda está fechada.")
        print("Derrote todos os inimigos de Alcântara para os mercadores confiarem em você.")
        return                                            # ENCERRA A FUNÇÃO E VOLTA AO MENU

    print(f"\n{AMARELO}===== FEIRA DE ALCÂNTARA ====={RESET}")
    print("1 - Comprar Poção SaBOUR Guaraná (10 grana)")
    print("2 - Comprar Adaga Cega da Feirinha (30 grana)")
    print("3 - Comprar Escudo de Porta de Van (40 grana)")
    print("4 - Sair")

    opcao = input("Escolha: ")                            # RECEBE A COMPRA ESCOLHIDA

    if opcao == "1":                                      # COMPRA DE POÇÃO
        if jogador["grana"] >= 10:                        # VERIFICA DINHEIRO PARA COMPRAR POÇÃO
            jogador["grana"] -= 10                        # DESCONTA O PREÇO DA POÇÃO
            inventario.append("Poção SaBOUR Guaraná")
            print("\nPoção SaBOUR Guaraná comprada!")
            print("'Pode causar nauseas, tonturas e visões estranhas', pelo menos era barato...")
        else:                                             # CASO NÃO SEJA O MAPA ATUAL
            print("\nSem nenhum tustão.") or print("\nVocê tá liso.") or print("\nVai ter que catar umas moedas no chão...")
            

    elif opcao == "2":                                    # COMPRA DA ADAGA CEGA DA FEIRINHA
        if jogador["grana"] >= 30:                        # VERIFICA DINHEIRO PARA COMPRAR ESPADA
            jogador["grana"] -= 30                        # DESCONTA O PREÇO DA ESPADA
            inventario.append("Adaga Cega da Feirinha")         # GUARDA A ESPADA NO INVENTÁRIO
            jogador["ataque"] += 5                        # AUMENTA O ATAQUE AO SUBIR DE NÍVEL
            print("\nAdaga Cega da Feirinha comprada!")
            print("Parece que vai quebrar fácil, mas pelo menos o ataque aumentou.")
            print("Ataque aumentado em +5!")
        else:                                             # CASO NÃO SEJA O MAPA ATUAL
            print("\nSem nenhum tustão.") or print("\nVocê tá liso.") or print("\nVai ter que catar umas moedas no chão...")

    elif opcao == "3":                                    # COMPRA DA ESCUDO DE PORTA DE VAN
        if jogador["grana"] >= 40:                        # VERIFICA DINHEIRO PARA COMPRAR ESCUDO
            jogador["grana"] -= 40                        # DESCONTA O PREÇO DO ESCUDO
            inventario.append("Escudo de Porta de Van")         # GUARDA O ESCUDO NO INVENTÁRIO
            jogador["vida_max"] += 20                     # AUMENTA BASTANTE A VIDA MÁXIMA
            jogador["vida"] = jogador["vida_max"]         # RESTAURA A VIDA AO MÁXIMO
            print("\nEscudo de Porta de Van comprado!")
            print("Meio suspeito, mas a vida agradece!")
            print("Vida máxima aumentada em +20!")
        else:                                             # CASO NÃO SEJA O MAPA ATUAL
           print("\nSem nenhum tustão.") or print("\nVocê tá liso.") or print("\nVai ter que catar umas moedas no chão...")

    elif opcao == "4":                                    # OPÇÃO PARA SAIR DA LOJA
        print("\nSaindo da loja...")

    else:                                                 # CASO NÃO SEJA O MAPA ATUAL
        print("\nOpção inválida.")


# ======================================
# MENU
# RESPONSÁVEL: KELLVYN
# CONTROLE GERAL DO JOGO
# ======================================

def menu():                                               # MENU PRINCIPAL QUE CONTROLA O FLUXO DO JOGO
    introducao()                                          # MOSTRA A INTRODUÇÃO ANTES DO JOGO COMEÇAR
    criar_personagem()                                    # CRIA O JOGADOR ANTES DA AVENTURA
    historia_mapa()                                       # MOSTRA A HISTÓRIA DO NOVO MAPA

    while True:                                           # REPETE ATÉ O JOGADOR ESCOLHER UMA OPÇÃO VÁLIDA
        mapa = mapas[mapa_atual]                          # PEGA O DICIONÁRIO COMPLETO DO MAPA ATUAL
        inimigos_restantes = len(mapa["inimigos"]) - len(mapa["derrotados"])  # CALCULA QUANTOS INIMIGOS FALTAM NO MAPA

        verificar_trapaca()                                  # CONFERE SE ALGUÉM TENTOU VIRAR LENDA NA BASE DA TRAPAÇA

        print(f"\n{AMARELO}===== TALES OF SG ====={RESET}")
        print(f"Mapa atual: {mapa['nome']}")              # MOSTRA ONDE O JOGADOR ESTÁ
        print(f"Inimigos restantes: {inimigos_restantes}")

        print("\n1 - Batalhar")

        if inimigos_restantes == 0 and not mapa["boss_derrotado"]:  # LIBERA O BOSS QUANDO TODOS OS INIMIGOS COMUNS ACABAM
            print("2 - Enfrentar boss")
        else:                                             # CASO NÃO SEJA O MAPA ATUAL
            print("2 - Enfrentar boss BLOQUEADO")
            

        print("3 - Avançar mapa")
        print("4 - Inventário")
        print("5 - Ver status")
        print("6 - Ver mapa")
        print("7 - Loja")
        print("8 - Sair")

        # ======================================
        # TRATAMENTO DE ERROS DO MENU PRINCIPAL
        # RESPONSÁVEL: KELLVYN
        # ======================================
        # O JOGO FOI FEITO PARA ENFRENTAR MONSTROS.
        # NÃO PARA ENFRENTAR QUEM DIGITA "ABUBEBLE" NO MENU.
        # ======================================

        try:
            escolha = int(input("Escolha: "))             # LÊ A ESCOLHA DO MENU COMO NÚMERO INTEIRO
        except ValueError:                                # CAPTURA ERRO CASO DIGITEM TEXTO NO LUGAR DE NÚMERO
            print("\nOpção inválida. Digite apenas números.")
            continue                                      # VOLTA PARA O COMEÇO DO MENU

        if escolha == 1:                                  # ABRE UMA BATALHA COMUM
            batalha()                                     # CHAMA A BATALHA CONTRA INIMIGO COMUM

        elif escolha == 2:                                # TENTA ENFRENTAR O BOSS
            batalha(boss=True)                            # CHAMA A BATALHA CONTRA BOSS

        elif escolha == 3:                                # TENTA AVANÇAR PARA OUTRO MAPA
            avancar_mapa()                                # CHAMA A FUNÇÃO DE PROGRESSÃO

        elif escolha == 4:                                # ABRE O INVENTÁRIO
            mostrar_inventario()                          # MOSTRA OS ITENS DO JOGADOR

        elif escolha == 5:                                # MOSTRA OS STATUS
            mostrar_status()                              # CHAMA A TELA DE STATUS

        elif escolha == 6:                                # MOSTRA O MAPA
            mostrar_mapa()                                # CHAMA A TELA DO MAPA

        elif escolha == 7:                                # ABRE A LOJA
            loja()                                        # CHAMA A LOJA DE ALCÂNTARA

        elif escolha == 8:                                # SAI DO JOGO
            print("\nFechando o jogo...")
            break                                         # SAI DO LAÇO QUANDO A ESCOLHA É VÁLIDA

        else:                                             # CASO NÃO SEJA O MAPA ATUAL
            print("\nOpção inválida.")


# ======================================
# INICIAR JOGO (CODIGO MAIS IMPORTANTE DE TODOS, NÃO APAGUE ISSO POR FAVOR)
# RESPONSÁVEL: EQUIPE
# INICIALIZAÇÃO DO PROGRAMA
# ======================================

menu()                                                    # INICIA O JOGO CHAMANDO O MENU PRINCIPAL
