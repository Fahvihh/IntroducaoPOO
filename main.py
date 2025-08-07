from Projeto_SICP.classes.ClasseFilhaPoderes import *
from Projeto_SICP.funcoes.Utilitarios import *

# Sistema Inteligente de Criação de Personagens com Perfil Psicológico

txt()
titulo("BEM-VINDO AO SICP -- SISTEMA INTELIGENTE DE CRIAÇÃO DE PERSONAGENS COM PERFIL PSICOLÓGICO")
txt()

escolha_nome = testestr("Deseja aleatorizar o nome de seu personagem? [S/N]: ")
personagem1 = ClassePoderes(escolha_nome)
personagem1.exibirinformacoes()

titulo("FIM! ESPERAMOS QUE TENHA SE DIVERTIDO!")



