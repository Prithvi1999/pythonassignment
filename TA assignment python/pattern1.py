def pattern1(k):
    s = 2*k - 2
    for i in range(0, k):
        for j in range(0, s):
            print(end=" ")
        s = s - 2
        for j in range(0, i+1):
            print("* ", end="")
        print("\r")

n = 5
pattern1(n)
