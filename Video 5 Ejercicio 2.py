def esprimo(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


print(esprimo(18))
print(esprimo(7))
print(esprimo(1))
print(esprimo(2))
print(esprimo(3))