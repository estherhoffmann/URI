#include <stdio.h>
#include <stdlib.h>

int intercala(int vetor[], int pos_comeco, int meio, int pos_final)
{
  int indice_prim_metade = pos_comeco;
  int indice_segun_metade = meio;
  int indice_aux = 0;
  int num_inv = 0;
  int tam = pos_final - pos_comeco;
  int *aux = malloc(tam*sizeof(int));

  while(indice_prim_metade < meio && indice_segun_metade < pos_final)
  {
    if(vetor[indice_prim_metade] < vetor[indice_segun_metade])
    {
      aux[indice_aux] = vetor[indice_prim_metade];
      indice_aux++;
      indice_prim_metade++;
    }
    else
    {
      aux[indice_aux] = vetor[indice_segun_metade];
      indice_aux++;
      indice_segun_metade++;
      num_inv += meio - indice_prim_metade;
    }
  }

  while (indice_prim_metade < meio)
  {
    aux[indice_aux] = vetor[indice_prim_metade];
    indice_aux++;
    indice_prim_metade++;
  }

  while (indice_segun_metade < pos_final)
  {
    aux[indice_aux] = vetor[indice_segun_metade];
    indice_aux++;
    indice_segun_metade++;
  }

  for(indice_aux = 0; indice_aux < tam; indice_aux++)
  {
    vetor[pos_comeco+indice_aux] = aux[indice_aux];
  }

  free(aux);
  return num_inv;
}

int contarInversoesR(int vetor[], int pos_comeco, int pos_final)
{
  int meio, num_inv = 0;

  if(pos_final - pos_comeco > 1)
  {
    meio = (pos_final + pos_comeco)/2;
    num_inv += contarInversoesR(vetor, pos_comeco, meio);
    num_inv += contarInversoesR(vetor, meio, pos_final);
    num_inv += intercala(vetor, pos_comeco, meio, pos_final);
  }
  return num_inv;
}

int contarInversoes_wrapper(int vetor[], int tam)
{
  return contarInversoesR(vetor, 0, tam);
}


int main()
{
  int qnt_testes, tam_vetor;
  int num_inv;
  if( scanf("%d", &qnt_testes) ) {};

  for(int i=0; i < qnt_testes; i++)
  {
    if( scanf("%d", &tam_vetor) ) {};

    int *vetor_inteiros = malloc(tam_vetor*sizeof(int));
    for(int j= 0; j < (tam_vetor); j++)
    {
      if( scanf("%d", &vetor_inteiros[j]) ) {};
    }

    num_inv = contarInversoes_wrapper(vetor_inteiros, tam_vetor);
    printf("Optimal train swapping takes %d swaps.\n", num_inv);
  }
  return 0;
}
