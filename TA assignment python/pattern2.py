def  pattern2(k):
    n = 65
    for i in range(0, k):
        for j in range(0, i+1):
            c = chr(n)
            print(c, end=" ")
            n = n +1
        print("\r")
        
pattern2(5)
