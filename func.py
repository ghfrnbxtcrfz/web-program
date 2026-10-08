def hello(username,age,country = "Россия"):
    print(f"Hello {username}, age: {age}, country: {country}")

hello("John",4)

hello(username='Vasya', age=28)

def print_numbers(*numbs):
    for n in numbs:
        print(n)

print_numbers(1,2,3,4,5)

def print_numbers(*numbs):
    a=0
    for n in numbs:
        a+=n
    print(a)

print_numbers(1,2,3,4,5)

def print_numbers(*numbs):
    a=0
    for n in numbs:
        #if n==3:
            #return a
        a+=n
    return a

print_numbers(1,2,3,4,5)
print(a)