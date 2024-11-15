# babylonian method for square root

base = 1
n = 0

# iterative method
# if n == 1 or n == 0:
#     print(n)
#     exit()
# for i in range(n):
#     base = (base + n/base) / 2
# print(base)

def root(base, n):
    if n == 1 or n == 0:
        return base
    if abs(n - base**2) < 0.0000001:
        return base
    else:
        return root((base + n/base)*0.5, n)

print(root(base, n))