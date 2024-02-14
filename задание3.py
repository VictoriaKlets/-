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
поиск вакансий в списке по названию компании.
переменная "с" отслеживает была ли найдена компания с ведённым названием
s - поступаемое название компании от пользователя
'''
s=''
while s!="None":
    s=str(input())
    c=0
    for i in range (0,len(a)-2):
        if a[i[0]]==s:
            print("В" + s + "найдена вакансия:" a[i[1]]+ ". З/п составит:" a[i[2]])
            c+=1
    if c==0: print("К сожалению, ничего не удалось найти")
