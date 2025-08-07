import time
nomesclasses = {1: "MAGO", 2: "GUERREIRO", 3: "CLÉRIGO", 4: "LADRÃO", 5: "DRUIDA", 6: "CAVALEIRO", 7: "FEITICEIRO",
                8: "ASSASSINO", 9: "ARQUEIRO"}

def mostrarclasses():
    espc()
    txt()
    titulo("ESCOLHA SUA CLASSE (PENSE BEM!)")
    txt()
    for k, valuer in nomesclasses.items():
        print(f"[{k}] - {valuer}")
        time.sleep(1)

def txt():
    print("-" * 95)

def txt1():
    print("*-" * 46)

def titulo(texto):
    print(f"{texto:^95}")

def espc():
    print("")

def testestr(P):
    while True:
        try:
            text = input(P).upper().strip()[0]
            if text in ("S", "N"):
                break
            else:
                print("Digite S ou N")
        except IndexError:
            print("Digite S ou N.")
    return text