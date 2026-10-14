# concurrent.futures: API para  executar tarefas em paralelo

import concurrent.futures as cf
import sys
import time

def fib(n):
    if n <= 2:
        return 1
    if n == 0:
        return 0
    if n < 0:
        raise Exception('fib(n) not defined for n < 0')
    return fib(n-1) + fib(n-2)

if __name__ == "__main__":
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 32
    n_procs = int(sys.argv[2]) if len(sys.argv) > 2 else 2

    assert n_procs >= 1, "Process number must be >= 1"

    print(f"calculando fib({n} em {n_procs} processo(s)...)", flush=True)

    t0 = time.perf_counter()

    with cf.ProcessPoolExecutor(max_workers=n_procs) as pool:
        results = list(pool.map(fib, [n] * n_procs))
    dt = time.perf_counter() - t0

    print(f"Resultado: fib({n}) = {results[0]}")
    print(f"Processos concluídos: {len(results)}")
    print(f"Tempo: {dt:.3f}s")
    print('OBS: vários processos calculam o mesmo fib - veja o pool')