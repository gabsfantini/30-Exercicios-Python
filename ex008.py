num = 29
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "não é primo")
            break
    else:
        print(num, "é primo")
else:
    print(num, "não é primo")
