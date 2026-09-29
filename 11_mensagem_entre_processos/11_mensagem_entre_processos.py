# um processo envia, outro responde — espírito MPI Send/Recv.
# Objetivo: enviar uma mensagem e receber eco entre
# processos (Send/Recv conceitual).
from multiprocessing import Process, Queue

def trabalhador(entra, sai):
    #get(): espera até chegar uma mensagem na fila "entra" 
    # Recv (receber)
    msg= entra.get()

    #put(): coloca a resposta na fila "sai"
    #equivale a ideia de Sendo (enviar)
    sai.put("eco:" +msg)

if __name__ =="__main__":
    entra,sai= Queue(),Queue() #queue ->fila de mensagens

    p=Process(target=trabalhador, args=(entra,sai))
    p.start()

    entra.put("Olá") 
    print(sai.get()) 

    p.join()