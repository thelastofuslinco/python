numero = int(input('digite um numero: '))
total = 0

for n in range(1, numero + 1):
    if n <= 1:
        continue

    eh_primo = True

    for i in range(2, int(n ** (1 / 2)) + 1):
        if n % i == 0:
            eh_primo = False
            break

    if eh_primo:
        print(f"{n} é primo.")
        total += 1

print(f"Total: {total}")
