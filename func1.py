#Задача №1
def my_sum(arr: list[float | int]) -> float | int:
    a=0
    for i in arr:
        a+=i
    return a
print(my_sum([1, 2, 3, 4, 5]))
print(my_sum([-1, -2, 3, -4, 5]))

#Задача №2
def my_avg(arr: list[float | int]) -> float | int:
    c=0
    a=0
    for i in arr:
        a+=i
        c+=1
    if c==0:
        return 0
    return a/c
print(my_avg([1, 2, 3, 4, 5]))
print(my_avg([20, 30, 3, 40, 5]))

#Задача №3
def my_min(arr: list[float | int]) -> float | int:
    if not arr:
        return None
    mini = arr[0]
    for i in arr:
        if i < mini:
            mini = i
    return mini
print(my_min([1, 2, 3, 4, 5]))
print(my_min([20, 30, 3, 40, 5]))

#Задача №4
def my_max(arr: list[float | int]) -> float | int:
    if not arr:
        return None
    maxi = arr[0]
    for i in arr:
        if i > maxi:
            maxi = i
    return maxi
print(my_max([3, 1, 4, 1, 5, 9, 2, 6])) 
print(my_max([-5, -1, -10, -3]))  

#Задача №5
def my_max_filter(arr: list[float | int], num: float | int) -> list[float | int]:
    result = []
    for i in arr:
        if i > num:
            result.append(i)
    return result
print(my_max_filter([1, 5, 3, 8, 2, 9], 4))    
print(my_max_filter([-5, -1, -10, -3], -2)) 

#Задача №6
def my_len(arr: list[float | int]) -> int:
    count = 0
    for i in arr:
        count += 1
    return count
print(my_len([1, 2, 3, 4, 5]))       
print(my_len([10, 20, 30]))         
print(my_len([1.5, 2.5])) 
