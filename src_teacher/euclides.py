# Def phi de euler

def phi(n):
    m=0
    for k in range(1,n):
        if eucides(n,k)==1:
            m=m+1
    return m

print()
