"""
print("Hello World!")
a = "Hello World!"
print(a)
b=43
print(b)
print(type(b))
e: bool =True
print(e)
print(a, type(b))
arr = [1,2,3,4,5,6]
print(arr[0])
arr[5] = 47
print(arr)
arr.append(12)
print(arr)
print(len(arr))

for i in (arr):
    print(i)

for i in (arr):
    print(f"Число: {i}")

n = 10
m = n+3
print(m)
"""
n=1
g=1
while n<10:
    while g<10:
        print(n*g,end='\t')
        g+=1
    n+=1
    g=1
    print('\n')


c1='hello'
for c in c1:
    print(c,end='\t')
print('\n')

c1 = 'ab'
c2 = 'cd'
for c in c1:
    for s in c2:
        print(f'{c}{s}')

for i in [1,2,3,4]:
    if i==3:
        break
    print(f"Number: {i}")

for i in [1,2,3,4]:
    if i==3:
        continue
    print(f"Number: {i}")

