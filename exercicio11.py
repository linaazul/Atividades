# Função que memoriza resultados
# Implemente uma função memorizador que retorna uma função capaz de armazenar resultados anteriores. Use closure para "lembrar" dos resultados já calculados.

# ATENÇÃO: NÃO consegui fazer essa atividade por motivos de: decorador.
# Pedi pro gpt fazer e explicar então essa atividade não foi feita por mim.
# Estou mandando no github pois é bom ver esse exemplo e entender quando precisar.

def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

# Função memorizadora


def memorizador(func):
    cache = {}  # Dicionário para armazenar os resultados já calculados

    def func_memorizada(n):
        if n in cache:  # Se o resultado já foi calculado, retorna do cache
            return cache[n]
        resultado = func(n)  # Se não, calcula o resultado
        cache[n] = resultado  # Armazena o resultado no cache
        return resultado

    return func_memorizada  # Retorna a função memorizada


fib_memorizado = memorizador(fib)

# Testando o Fibonacci memorizado
print(fib_memorizado(10))  # O cálculo do Fibonacci de 10 será memorizado.
