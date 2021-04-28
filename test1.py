l=[10, 15, 3, 7]
k=int(input())
i=0
while(i<len(l)):
    j=1
    while(j<=len(l)-1):
        if(l[i]+l[j]==k):
            print('True',l[i],l[j])
            break
        j=j+1
    i=i+1