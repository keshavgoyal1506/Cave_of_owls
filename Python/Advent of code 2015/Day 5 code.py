x=open("All Inputs.txt",'r')
while x.readline()!='Day 5\n' :
    continue
ncounto=0
ncountn=0
for i in range(1000):
    vcount=0
    flag=False
    flag2=False
    flag3=False
    flag4=False
    a=x.readline()
    c=['.']
    for j in range(15):
        b=a[j]+a[j+1]
        if b in ('ab','cd','pq','xy'):
            flag=True
            break
        if flag2==False and b[0]==b[1]:
            flag2=True
        if b[0] in ('a','e','i','o','u'):
            vcount+=1
        if flag3==False and b in c[:-1]:
            flag3=True
        if flag4==False and c[-1][0]==b[1]:
            flag4=True       
        c.append(b)
    if flag3==True and flag4==True:
        ncountn+=1
    else:
        print(a,c)
    if b[1] in ('a','e','i','o','u'):
        vcount+=1
    if flag==False and flag2==True and vcount>=3:
        ncounto+=1
print('There are',ncounto,'number of nice strings.')
print('With the new rules we will have',ncountn,'number of nice strings')
x.close()
            
        
        
    
    
