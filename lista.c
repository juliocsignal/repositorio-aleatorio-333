#include <stdio.h>
#include <conio.h> //Se estiver em ambiente Linux, comente esta linha por completo
#include <locale.h>

int main()
{
	setlocale(LC_ALL,"");

	int numeros[10];
	int positivos=0;
	int i;
	int pares = 0;
	float media = 0;

	for(i=0;i<10;i++)
	{
		printf("Digite um n�mero: ");
		scanf("%d",&numeros[i]);
	}
	
	for(i=0;i<10;i++)
	{
		if(numeros[i] % 2 == 0)
		{
			pares++;
		}
		if(numeros[i]>0)
		{
			positivos = positivos + 1;
		}
		printf("%d� N�mero:  %d\n",i+1,numeros[i]);
		media = media + numeros[i];
	}
	printf("\nExistem %d n�meros pares nessa lista!\n",pares);
	printf("A m�dia dos n�meros digitados �: %f\n",media/10);
	printf("Existem %d n�meros positivos nessa lista!",positivos);

	getch();	//Se estiver em ambiente Linux, comente esta linha por completo

	return 0;
}