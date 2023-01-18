import requests
from bs4 import BeautifulSoup
from sklearn import datasets

#1 на базе данных введенных вручную
my_list = [int(el) for el in "1 2 3 4 5 6 7 8 9".split()]
my_list_squared = map(lambda num: num +3*4, my_list)

print(my_list)
print(list(my_list_squared))


