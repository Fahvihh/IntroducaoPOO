from Projeto_SICP.funcoes.Utilitarios import *
import random
import time

class Personagem():
    def __init__(self, escolha_nome):
        if escolha_nome == "S":
            self.__nome = self.sorteia_nome().capitalize().strip()
            espc()
            titulo("O nome do personagem é...")
            espc()
            time.sleep(1)
            txt()
            titulo(f"{self.__nome}")
            txt()
        else:
            while True:
                self.__nome = input("Insira o nome do personagem: ").strip().capitalize()
                if self.__nome:
                    break
                else:
                    print("Digite um nome válido!")
            espc()
            titulo("O nome do personagem é...")
            espc()
            time.sleep(1)
            txt()
            titulo(f"{self.__nome}")
            txt()

        alterar = testestr("Deseja alterar o nome de seu personagem? [S/N]: ")
        if alterar == "S":
            while True:
                novo_nome = input("Insira o novo nome de seu personagem: ").strip().capitalize()
                if novo_nome:
                    self.__nome = novo_nome
                    espc()
                    titulo("O nome do personagem é...")
                    espc()
                    time.sleep(1)
                    txt()
                    titulo(f"{self.__nome}")
                    txt()
                    break
                else:
                    print("Nome inválido. Tente novamente.")

        while True:
            self.idade = input("Digite a idade do personagem: ").strip()
            if self.idade.isnumeric():
                self.idade = int(self.idade)
                break
            else:
                print("Idade Inválida. Tente novamente.")


        while True:
            try:
                mostrarclasses()
                espc()
                self.classe = int(input("Insira a classe de seu personagem: "))
                if not 1 <= self.classe <= 9:
                    print("Erro! Número não está na lista, tente novamente.")
                else:
                    break
            except ValueError:
                print("Valor digitado não é um número inteiro. Tente novamente.")

    @staticmethod
    def sorteia_nome():
        with open("dados/nomes.txt", "r", encoding="utf-8") as arquivo:
            nomes = [linha.strip() for linha in arquivo if linha.strip()]
        return random.choice(nomes)

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome