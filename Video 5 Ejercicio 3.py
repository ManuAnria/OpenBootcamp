def esbisiesto(year):
    if year % 4 == 0:
        return True
    else:
        return False


print(esbisiesto(2020))
print(esbisiesto(2022))
print(esbisiesto(2024))