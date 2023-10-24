
primos = []

for num in range(1,999):
    ##print(num)

    eh_primo = True

    i = 2
    while i <= num // 2:
        if num % i == 0:
            eh_primo = False
            break
        i += 1

    if eh_primo:
        primos.append(num)

print(primos)