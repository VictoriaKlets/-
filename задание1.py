import csv

'''
чтение таблицы vacancy.csv без строки заголовков
'''
with open("vacancy.csv" , "r", encoding = "utf-8", newline = "") as f:
    table = list(csv.reader(f, delimiter = ","))[1:]

'''
добавление столбцов company, role, Salary в отдельный список a
'''
a=[]
for i in table:
    a=[i[4], i[3],i[0]]

'''
создание списка с. Нахождение вакансии с самой большой зарплатой в компании
'''

c=[]
for y in range(0, len(a)-2):
    b=0
    for u in range(1,len(a)-2):
        b=int(a[y[2]])
        if a[y[0]] == a[u[0]]:
            if int(a[y[2]])<int(a[u[1]]): b=a[u[2]]
    c=[y[0],y[1],b]

with open("vacancy_new",'w', encoding="utf-8") as f2:
    writer
    


    
