def discriminant(a, b, c): 
    D = b**2 - 4*a*c 
    if D < 0:
        return ("действительных корней нет")  # действительных корней нет
    elif D == 0:
        x = -b / (2*a)
        return (x)
    else:
        sqrt_D = D**0.5
        x1 = (-b + sqrt_D) / (2*a)
        x2 = (-b - sqrt_D) / (2*a)
        return (x1, x2)

print(discriminant(2,-4,2))
print(discriminant(4,-3,1))
print(discriminant(6,1,-1))

def vieta(a, b, c):
    p = b / a
    q = c / a

    q_abs = abs(int(q))
    for d in range(1, q_abs + 1):
        if q_abs % d != 0:          # d — не делитель, пропускаем
            continue
        for x1 in (d, -d):          # пробуем +d и -d
            x2 = q / x1
            if x1 + x2 == -p:
                return (x1, x2)


    return ("целых корней не нашлось")   


print(vieta(1, -5, 6))   
print(vieta(1, 2, 1))   
print(vieta(1, 3, 2))    