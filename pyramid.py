##pyramid problem

def pyramid(a):
    
    ls=[]
    b=a
    j=a
    for i in range(0,a):
        n=a
        while n>=1:
            if j<b:
                k=b-j
                while k>=1:
                    ls.append(" ")
                    k=k-1
                    j=j+1
            ls.append(n)
            n=n-1
        print(*ls)
        ls=[]    
        a=a-1
        j=a

tt=input("input number to start pyramid :")
pyramid(int(tt))