# Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. 
# Por exemplo: 127 -> 721.def reverso(entrada):

  texto = str(entrada)
  numeroReverso = ''

  for i in range(len(texto),0,-1):
    numeroReverso += texto[i-1]

  return numeroReverso


entrada = int(input('Insira um número inteiro: '))
saida = reverso(entrada);

print('O número reverso do número inteiro digitado é: ',end='')
print(saida)
