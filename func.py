"""
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
"""
"""
def print_kwargs(**kwargs):
   # print(type(kwargs))
    print(kwargs)

print_kwargs(
    a='hello',
    b='world',
    c='Tomsk',
)

name ="John"
age = 28
lastname = "mir"
work = "teacher"

people = {
    'name': 'John',
    'age': 28,
    'lastname': "mir",
    'job': 'teacher'
}
print(people['name'])

person_data={
    "person":{
        "name":"Ипатий",
        "last_name":"Streich",
        "middle_name":"Азарий",
    },
    "company":{
        "post":"менеджер",
        "company_name": "ОАС ДудинкаТрейдРус"
    },
    "address":{
        "street":"Nikitina",
    }
}
print(person_data['person']["name"])

#print_kwargs(**person_data)

if "address" in person_data:
    print(person_data["address"])
else:
    print("No address")

print(
    person_data.get("person")
)

person_data["education"]={
    "school":"high",
    "course": 4,
}
print(person_data.keys())
print("*"*10)
print(person_data.values())

person_data["person"]["iast_name"]="Adbraham"
print(person_data)

del person_data["address"]
print(person_data)
"""
a=5
print(a**2)
b=25**0.5
print(b)