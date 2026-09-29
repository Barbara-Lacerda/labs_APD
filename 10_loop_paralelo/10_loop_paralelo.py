from threading import Thread
# reparte um loop independente — espírito OpenMP parallel for.
# objetivo:somar vetores com loop fatiado em 2 workers
# e comparar com sequencial.

a=[10, 20, 30, 40, 50, 60]
n= len(a)
meio=n // 2 #// divide sem "valor quebrado" 
somas=[0,0]

def esquerda():
    for i in range(0,meio):
       somas[0]= somas[0] + a[i]#[60]

def direita():
    for i in range(meio,n):
         somas[1]= somas[1] + a[i]#[150]

t1=Thread(target=esquerda)
t2=Thread(target=direita)

t1.start()
t2.start()
t1.join()
t2.join()

print(somas) 
print(somas[0] +somas[1])