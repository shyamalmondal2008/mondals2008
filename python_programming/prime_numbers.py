def isprime():
    num = int(input("please provide the input: "))
    for i in range(2, num):
        if (num % i) == 0:
            print("Not Prime")
            break
    else:
        print("prime")


isprime()
