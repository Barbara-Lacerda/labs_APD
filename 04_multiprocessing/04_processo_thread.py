# Objetivo: ver memória compartilhada (threads) versus
# isolamento (processos / workers).

# threads no MESMO processo(memória compartilhada)
import threading

# multiprocessing: processos SEPARADOS (memória isolada + fila)
import multiprocessing as mp
import os #permite usar comando do SO

contador = 0 

def soma_thread():
    global contador # faz sentido trabalhando com thread
    contador += 1
    print(
        f"[thread] pid={os.getpid()} ident={threading.get_ident()}"
        f"contador={contador}",
        flush=True  #idependente de onde tiver no código vai executar o print exatamente 
        # na hora que ele chegar no print, "garantir" tempo paramostrar a mensagem
        # na hora que ele chegar no print, "garantir" tempo paramostrar a mensagem
          )

def soma_processo(saida):
    n = 1
    print(
        f"[processo] pid={os.getpid()} n={n}"
        f"(cópia local de contador={contador})",
        flush=True
    )
    saida.put(n)

if __name__ =="__main__":
    print('pid da MAIN', os.getpid(), flush=True)
    print(flush=True)

    print("THREADS: mesma memória(mesmo PID, ident difetente)")
    t1 = threading.Thread(target=soma_thread)
    t2 = threading.Thread(target=soma_thread)
    t3= threading.Thread(target=soma_thread)
    t4= threading.Thread(target=soma_thread)

    #start(): dispara o fluxo. Não cria um novo processo no SO
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    print('contador na main: ', contador, flush=True)

    #PROCESSOS: vamos trabalhar com processos diferentes; e trocas de mensagens

    print("PROCESSOS: memória isolada (PID novo; main não vê n)")
    fila = mp.Queue()           #cria uma fila
    p1 = mp.Process(target=soma_processo, args=(fila,))  #(fila,) -> indica que estou trabalhando c/ TUPLA
    p2 = mp.Process(target=soma_processo, args=(fila,))  # tupla em py é usado como se fosse um vetor

    p1.start()
    p2.start()
    #get(): BLOQUEIA até cada filho colocar o valor na variável
    #isso é a comunicação
    a = fila.get()
    b = fila.get()
    p1.join()
    p2.join()
    print("Contador main: ",contador,flush=True)
    print("Cada processo devolveu: ",a,'e',b,flush=True)

