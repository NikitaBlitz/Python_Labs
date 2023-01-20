from pyDatalog import pyDatalog

summ = ((0 + 999999) * 1000000) / 2
median = 100 / 2

pyDatalog.create_terms('Sum_n, Avg, Median, Prod_n') # Создаем термы Sum_n, Avg, Median, Prod_n
pyDatalog.create_terms('factorial, N') # Создаем терм factorial и N
factorial[N] = N * factorial[N - 1] # Определяем факториал как рекурсивное выражение
factorial[1] = 1

print((Sum_n == summ)&(Avg == Sum_n/1000000)&(Median == median))
print()
print(Prod_n == factorial[100])
