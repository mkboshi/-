# Импортировать объект-шаблон из модуля jinja2 
from jinja2 import Template
import matplotlib.pyplot as plt 

# Описать функцию, в качестве параметра передать значение аргумента x 
# функция должна возвращать значение заданной функции, вычисленной от x 
def f(x):
    y = x*x*x - 6*x*x + x + 5
    return y

def create_pict(x, y): 
     
    #Построить линию графика, установить для нее цвет и толщину: 
    line = plt.plot(x, y) 
    plt.setp(line, color="blue", linewidth=2)
 
    # Вывести 2 оси, установить их в позицию zero: 
    plt.gca().spines["left"].set_position("zero") 
    plt.gca().spines["bottom"].set_position("zero") 
    plt.gca().spines["top"].set_visible(False) 
    plt.gca().spines["right"].set_visible(False) 
     
    # Сохранть результат построения в файл: 
    plt.savefig("pict.jpg") 
     
    # Вернуть имя созданного файла 
    return "pict.jpg" 

 
# Задать начало a и конец  b интервала построения функции, 
# количество точек построения.  
a = -2 
b = 6 
n = 30 
 
# Вычислить шаг 
h = (b - a) / n
 
# Сформировать список со значениями аргумента  
x_list = []
for i in range(0, n+1):
    x_list.append(a + i*h)
 
# Сформировать список со значениями функции для  
# каждого элемента списка x_list
f_list = []
for x in x_list:
    f_list.append(f(x))

name_pict = create_pict(x_list, f_list)
 
# Прочитать шаблон из файла function_template.html 
f_template = open('function_template.html','r', encoding ='utf-8-sig') 
html = f_template.read() 
f_template.close() 
 
# Создать объект-шаблон 
template = Template(html) 
# Указать, что в шаблоне будет использована функция len 
template.globals["len"] = len
template.globals["round"] = round
 
#Cоздадать файл для HTML-страницы 
f = open('function.html', 'w', encoding ='utf-8-sig')

# Сгенерировать страницу на основе шаблона 
result_html = template.render(x = x_list,
                              y = f_list,
                              pict = name_pict
                              ) 
# Вывести сгенерированную страницу в файл 
f.write(result_html) 
f.close()
