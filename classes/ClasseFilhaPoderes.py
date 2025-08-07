from Projeto_SICP.classes.ClasseMaePersonagem import *
from Projeto_SICP.funcoes.teste_psicologico import *

class ClassePoderes(Personagem):
    def __init__(self, escolha_nome):
        super().__init__(escolha_nome)
        if self.classe == 1:
            self.ataque = 50
            self.defesa = 80
            self.perfil = ("Um mestre dos segredos arcanos, o mago canaliza o poder dos "
                           "elementos e do conhecimento \nantigo para lançar feitiços devastadores.")

        elif self.classe == 2:
            self.ataque = 80
            self.defesa = 60
            self.perfil = ("Um combatente feroz treinado no campo de batalha, o guerreiro"
                           " luta com força bruta e \ncoragem, sempre na linha de frente.")

        elif self.classe == 3:
            self.ataque = 40
            self.defesa = 90
            self.perfil = ("Guiado pela fé, o clérigo conjura luz e cura, protegendo seus"
                           " aliados e punindo o mal \ncom a força divina.")

        elif self.classe == 4:
            self.ataque = 55
            self.defesa = 70
            self.perfil = ("Ágil e furtivo, o ladrão vive nas sombras. Especialista em "
                           "emboscadas, armadilhas e \nhabilidades evasivas.")

        elif self.classe == 5:
            self.ataque = 56
            self.defesa = 90
            self.perfil = ("Guardião da natureza, o druida invoca as forças do mundo "
                           "selvagem para curar, proteger \ne atacar com fúria natural.")

        elif self.classe == 6:
            self.ataque = 88
            self.defesa = 49
            self.perfil = ("Um cavaleiro sagrado que mistura força e fé. Luta pelo bem com "
                           "sua espada justa e sua \ndevoção inabalável.")

        elif self.classe == 7:
            self.ataque = 69
            self.defesa = 80
            self.perfil = ("Diferente do mago, o feiticeiro nasceu com a magia correndo"
                           " em suas veias. Seu poder\né instintivo e imprevisível.")

        elif self.classe == 8:
            self.ataque = 65
            self.defesa = 60
            self.perfil = ("Silencioso e mortal, o assassino elimina seus alvos com precisão"
                           " cirúrgica, sem deixar \nrastros.")

        elif self.classe == 9:
            self.ataque = 90
            self.defesa = 50
            self.perfil = ("Especialista em ataques à distância, o arqueiro combina visão"
                           " aguçada e mira certeira\npara derrubar inimigos antes mesmo de se aproximarem.")

        txt1()
        titulo(nomesclasses[self.classe])
        txt1()
        print(f"---> {self.perfil}")
        self.personalidade = DefinaPersonalidade()

    def exibirinformacoes(self):
        espc()
        titulo("Personagem criado com sucesso!! Parabéns! Segue abaixo seu perfil...")
        espc()
        time.sleep(2)
        txt1()
        titulo(f"O {nomesclasses[self.classe].capitalize()} {self.nome.capitalize()} --> {self.personalidade[0]} ")
        txt1()
        espc()
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"classe: {nomesclasses[self.classe]}")
        print(f"Ataque: {self.ataque}")
        print(f"Defesa: {self.defesa}")
        espc()
        txt1()
        espc()
        print(f"Descrição da Classe:\n{self.perfil}")
        espc()
        txt1()
        print(f"Perfil Psicológico: {self.personalidade[0]}")
        txt1()
        espc()
        print(f"Descrição Psicológica:\n{self.personalidade[1]}")
        espc()
        txt1()
