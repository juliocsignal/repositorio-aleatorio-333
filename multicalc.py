# -*- coding:utf-8 -*-
from opcoes import opcao1
from opcoes import opcao2
from opcoes import opcao3

opcao = input("O que você quer fazer agora?\n1 - Equação do Segundo Grau \n2 - Calcular contas do mês\n3 - Jogar 'Desafio Random' ")

if (opcao == "1"):
    opcao1.EqSegGrau()

if (opcao == "2"):
    opcao2.CalcMes()

if (opcao == "3"):
    opcao3.Sorte()
