# За день машина проезжает N километров. Сколько дней нужно, чтобы проехать маршрут длиной M километров?

# Формат ввода

# Программа получает на вход числа N и M (целые, положительные).

N, M = int(input()), int(input())

print(M // N + (1 - 0**(M % N)))
