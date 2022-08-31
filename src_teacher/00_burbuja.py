def burbuja(a):
    for i in range(len(a)-1,0,-1):
        print(i, " comparaciones")
        for j in range(i):
            if a[i] < a[j]:
                t = a[i]
                a[i] = a[j]
                a[j] = t
    return a

print(burbuja([8,1,5,3,2]))
