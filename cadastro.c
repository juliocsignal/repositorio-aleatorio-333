#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <conio.h>

//Codificação em UTF-8

int main()
{
	FILE*arq;
	char nome[1000];
	int pecasvend,faltas;
	float salario,salariobruto,descontos;

	arq = fopen("folha_de_pagamento.txt","a+");

if(arq != NULL)
{
	printf("Digite o nome do funcionario: ");
	scanf("%s",&nome);
	printf("Qual e o salario bruto do funcionario? ");
	scanf("%f",&salariobruto);
	printf("Quantas pecas ele vendeu? ");
	scanf("%d",&pecasvend);

	printf("Quantas faltas ele teve? ");
	scanf("%d",&faltas);
	
	descontos = faltas*(salariobruto*0.05);

	salario = pecasvend * 15 + salariobruto - descontos;
	
	//printf("O funcionario recebera %.2f, pois faltou %d vezes e vendeu %d pecas!",salario,faltas,pecasvend);
	fprintf(arq,"\n\nFuncionario: %s\nSalario Bruto: %.2f\nPecas Vendidas: %d\nFaltas: %d\nSalario Final: %.2f\n\n\n",nome,salariobruto,pecasvend,faltas,salario);
}

else
{
	printf("ARQUIVO NULO!");
}	
	

	getch();
	
	fclose(arq);

	return 0;
}