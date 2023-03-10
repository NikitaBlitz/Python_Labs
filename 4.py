import requests
from bs4 import BeautifulSoup
from sklearn import datasets

#1 на базе данных введенных вручную
my_list = [int(el) for el in "1 2 3 4 5 6 7 8 9".split()]
my_list_squared = map(lambda num: num +3*4, my_list)

print(my_list)
print(list(my_list_squared))


#2 на базе данных полученных при парсинге
URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")  # Создаем объект BeautifulSoup для парсинга HTML-контента
results = soup.find(id="ResultsContainer")  # Находим элемент с id "ResultsContainer"
job_elements = results.find_all("div", class_="card-content") # Находим все элементы с классом "card-content" внутри элемента results
jobs= []
for job in job_elements:
    title_element = job.find("h2", class_="title") # Находим элемент с классом "title"
    jobs.append(title_element.text.strip())

print(jobs)
jobs= map(len,jobs)
print(list(jobs))

# 3 на базе данных из датасета
iris = datasets.load_iris()
listt = list(iris.target_names) # преобразуем целевые имена в список
print(listt)
x = map(len, listt)
print(list(x))