#aula Arquiteturas Paralelas e distribuídas 15/09
# Objetivo: comparar operação vetorial (SIMD-like) com
# três tarefas distintas (MIMD-like).
import time
from concurrent.futures import ThreadPoolExecutor

#PARTE 1 - SIMD (Single Instruction Multiple Data)
def estilo_simd():
    # montar uma linha com 60 sinais de iguais (só para quebrar nosso exemplo)
    print('=' * 60)
    print('PARTE 1- Estilo SIMD')
    print('Uma única operação: dobrar cada número.')
    print('=' * 60)

    numeros = [1,2,3,4,5]

    print(f'Dados de entrada: {numeros}')
    print('Instrução única: resultado = número * 2')
    print()
#momento de início do meu processamento
    t0 = time.perf_counter() #perf_counter -> precisão 
    
    dobrados = [n * 2 for n in numeros] #para cada n em números mult. por 2 e cria nova lista

#tempo de processamento 
    tempo = time.perf_counter() - t0
    print('Passo a passo mentalmente: ')
    for n, resultado in zip(numeros, dobrados): #zip -> permite colocar 2 listas emparelhadas, devem ser iguais(tam)
        print(f'{n} * 2 = {resultado}')

    print()
    print(f'Resultado final: {dobrados}')
    print(f'Tempo: {tempo:.6f}s')     #.6f ->mostrao tempo c/ 6 casas decimais
    

