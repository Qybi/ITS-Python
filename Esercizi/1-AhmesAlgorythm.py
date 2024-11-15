a,b,r = 27, 14, 0

# Ahmes Algorythm
while a >= 1:
    if a == 1:
        if r == 0:
            print(f"End: {a} * {b}")
        else:
            print(f"End: {a} * {b} + {r} = {a*b+r}")
        break
    elif a % 2 == 0:
        if r == 0:
            print(f"{a} è pari: \t \t {a}/2 * 2*{b} = ")
        else:
            print(f"{a} è dispari: \t \t ({a} - 1) * {b} + {b+r}")
        a = a // 2
        b = b * 2
    else:
        if r == 0:
            print(f"{a} è dispari: \t \t ({a} - 1) * {b} + {b}")
        else:
            print(f"{a} è dispari: \t \t ({a} - 1) * {b} + {b+r}")
        r = r + b
        a = a - 1
        