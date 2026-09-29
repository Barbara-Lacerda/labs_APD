# união dos laboratórios 10 e 11 - paralelismo com troca de mensagens.
# Objetivo: somar um vetor fatiado dividindo o trabalho em 2 processos (workers).
# Os workers calculam as somas parciais e enviam os resultados ao processo
# principal através de uma fila de mensagens (Queue), sem usar memória compartilhada.
from multiprocessing import Process, Queue

def somar_fatia(fatia, fila_saida):
    # O processo calcula a soma apenas da sua parte
    soma_local = 0
    for valor in fatia:
        soma_local += valor
    
    # Envia o resultado como uma mensagem para o processo principal
    fila_saida.put(soma_local)

if __name__ == "__main__":
    a = [10, 20, 30, 40, 50, 60]
    n = len(a)
    meio = n // 2
    
    # Separar as fatias do vetor para cada processo
    fatia_esquerda = a[:meio]
    fatia_direita = a[meio:]
    
    # Fila para recolher as mensagens (somas parciais)
    fila_resultados = Queue()
    
    # Criar os processos, passando a fatia e a fila de comunicação
    p1 = Process(target=somar_fatia, args=(fatia_esquerda, fila_resultados))
    p2 = Process(target=somar_fatia, args=(fatia_direita, fila_resultados))
    
    # Iniciar os processos
    p1.start()
    p2.start()
    
    # Aguardar e receber as mensagens da fila
    # Nota: A ordem em que os resultados chegam pode variar
    resultado_a = fila_resultados.get()
    resultado_b = fila_resultados.get()
    
    # Garantir que os processos terminaram
    p1.join()
    p2.join()
    
    # O processo principal faz a soma final
    soma_total = resultado_a + resultado_b
    
    print(f"Somas parciais recebidas nas mensagens: {resultado_a} e {resultado_b}")
    print(f"Soma total: {soma_total}")