#Задача №1
arr=[1,2,3,4,5,10,19,25,88,100]
summ=0
for i in arr:
    if i % 5 == 0:
        summ+=i
print(summ)
