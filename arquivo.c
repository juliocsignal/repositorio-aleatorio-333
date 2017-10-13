#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <conio.h>

//Codificação em UTF-8

int main()
{
	FILE*arq;
	float a,b,c;
	float delta,x1,x2;

	arq = fopen("arquivo.txt","w");

	printf("Digite o primeiro coeficiente: ");
	scanf("%f",&a);
	printf("Digite o segundo coeficiente: ");
	scanf("%f",&b);
	printf("Digite o terceiro coeficiente: ");
	scanf("%f",&c);
	
	if(a!=0)
		{
			delta = b * b - 4 * a * c;

		printf(arq,"Delta igual a: %f\n",delta);

		if(delta==0)
			{
				x1 = (-b)/(2*a);
				fprintf(arq,"So existe uma raiz! \\o/");
				fprintf(arq,"A raiz é: %f!\n",x1);	
			}
		else if(delta>0)
			{
				fprintf(arq,"Existem duas raizes! *-*\n");
				x1 = (-b+sqrt(delta))/(2*a);
				x2 = (-b-sqrt(delta))/(2*a);
				fprintf(arq,"As raizes sao: %f e %f",x1,x2);
			}
		else
			{
				fprintf(arq,"Não existem raizes reais! :'(");
			}
		}
	else
		{
			fprintf(arq,"Isso e uma equacao de primeiro grau, ANIMAL!");
		}



	getch();

	return 0;
}