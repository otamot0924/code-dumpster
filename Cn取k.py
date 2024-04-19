while True:
    n, k = list(input("C_取_：").split())

    if n == "天" and k == "經":
        print("吱吱")
    elif n == "望你" and k == "我":
        print("<3")
    else:
        n = int(n)
        k = int(k)

        if n<k:
            print("invalid input")
        else:
            n2 = 1
            k2 = 1
            count = 0

            while count != k:
                n2 *= n
                n -= 1
                count += 1

            for i in range(1,k+1):
                k2 *= i

            print(round(n2/k2))
