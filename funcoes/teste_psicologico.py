import time
from Projeto_SICP.funcoes.Utilitarios import *

def DefinaPersonalidade():
    time.sleep(7)
    espc()
    txt()
    titulo("TESTE PSICOLÓGICO: Como seu personagem reagiria?!")
    txt()
    time.sleep(1)
    P1 = testestr("01 - Seu personagem age por impulso quando está sob pressão? [S/N]: ")
    P2 = testestr("02 - Ele se sente mais produtivo trabalhando em equipe? [S/N]: ")
    P3 = testestr("03 - Ele evita compartilhar seus sentimentos com os outros? [S/N]: ")
    P4 = testestr("04 - Seu personagem quebraria regras se acreditasse que está fazendo o certo? [S/N]: ")
    P5 = testestr("05 - Ele costuma planejar tudo antes de agir? [S/N]: ")
    P6 = testestr("06 - Seu personagem usaria manipulação se fosse necessário para alcançar seus objetivos? [S/N]: ")
    print("ANALISANDO...")
    time.sleep(1)
    print("BUSCANDO ARQUETÍPOS...")
    time.sleep(1)
    espc()
    titulo("O resultado é...")
    espc()
    if P1 == "S" and P2 == "N" and P3 == "S" and P4 == "S" and P5 == "N" and P6 == "S":
        tipo = "🐺 O Rebelde Estratégico"
        desc = "Esse personagem é guiado pelos próprios ideais e não hesita em manipular o sistema se for\npreciso. Impulsivo, idealista e estrategista, ele representa o caos com propósito."

    elif P1 == "N" and P2 == "S" and P3 == "N" and P4 == "N" and P5 == "S" and P6 == "N":
        tipo = "🛡 O Protetor Cauteloso"
        desc = "Esse personagem prioriza o bem coletivo. Racional, cooperativo e cauteloso, ele planeja bem\ncada passo para garantir que ninguém fique para trás."

    elif P1 == "S" and P2 == "N" and P3 == "S" and P4 == "S" and P5 == "S" and P6 == "S":
        tipo = "🧠 O Estrategista Solitário"
        desc = "Reservado, independente e estratégico, esse personagem prefere agir pelas sombras. Ele confia\napenas em si mesmo — e isso o torna imprevisível e perigoso."

    elif P1 == "S" and P2 == "N" and P3 == "S" and P4 == "S" and P5 == "N" and P6 == "N":
        tipo = "🌪 O Instável Impulsivo"
        desc = "Esse personagem age sem pensar e não gosta de depender de ninguém. Espontâneo, impulsivo e \nsolitário, suas ações são tão imprevisíveis quanto ele mesmo."

    else:
        tipo = "🌀 O Ambíguo"
        desc = "Esse personagem não se encaixa em um único arquétipo. Cheio de nuances, pode reagir de \nformas diferentes conforme a situação. Essa ambiguidade o torna um personagem complexo — e talvez \no mais interessante de todos."

    txt()
    titulo(tipo)
    txt()
    print(f"---> {desc}")
    txt()
    time.sleep(7)
    return tipo, desc
