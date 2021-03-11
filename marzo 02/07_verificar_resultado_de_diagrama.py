a = int(input("Digite un valor : "))
b = int(input("Digite un valor : "))
c = int(input("Digite un valor : "))

if a > b:
    if a > c:
        if b > c:
            print("A:"+str(a))
            print("B:"+str(b))
            print("C:"+str(c))
        else:
            print("A:"+str(a))
            print("C:"+str(c))
            print("B:"+str(b))
    else:
        print("C:"+str(c))
        print("A:"+str(a))
        print("B:"+str(b))
else:
    if b > c:
        if a > c:
            print("B:"+str(b))
            print("A:"+str(a))
            print("C:"+str(c))
        else:
            print("B:"+str(b))
            print("C:"+str(c))
            print("A:"+str(a))
    else:
        print("C:"+str(c))
        print("B:"+str(b))
        print("A:"+str(a))
