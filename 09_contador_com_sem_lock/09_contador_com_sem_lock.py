#SEM  lock o total cai; COM o lock fica aberto
# Objetivo: ver ERRO sem lock e OK com lock (bemsimples).
import multiprocessing as mp

N=80_000

def sem_lock(contador):
    for _ in range(N):  # _ in -> convençaõ do python quando não vai usar variável como i
        contador.value = contador.value + 1

def com_lock(contador, lock):
    for _ in range(N):
        with lock: # exclusão mútua
            contador.value = contador.value + 1 #aqui vira secão crítica

def dois_processos(alvo, *extra):  #*extra -> usado quando trabalhamos com lock
    contador = mp.Value('i',0)  #mp. -> memória compartilhada, todos os processos consegue ler a variável
    p1 = mp.Process(target=alvo, args=(contador, *extra))
    p2 = mp.Process(target=alvo, args=(contador, *extra))
    p1.start()
    p2.start()
    p1.join()  # relembrando que o join serve para esperar
    p2.join()

    return contador.value

if __name__=="__main __":
    print("Esperado: ", 2*N)
    print("Sem lock: ",dois_processos(sem_lock))
    print("Com lock: ",dois_processos(com_lock, mp.Lock()))