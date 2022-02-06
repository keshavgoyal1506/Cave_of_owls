x=open("All Inputs.txt",'r')
while x.readline()!='Day 6\n' :
    continue
a=[]
d=[]
for i in range(1000):
    b=[]
    e=[]
    for i in range(1000):
        b.append(False)
        e.append(0)
    a.append(b)
    d.append(e)
for i in range(300):
    c=x.readline()
    c=c.split(" ")
    if c[0][1]=="u":
        if c[1][1]=="n":
            p=int(c[2].split(",")[0])
            q=int(c[2].split(",")[1])
            r=int(c[4].split(",")[0])
            s=int(c[4].split(",")[1])
            for i in range(p,r+1):
                for j in range(q,s+1):
                    a[i][j]=True
                    d[i][j]+=1
        else:
            p=int(c[2].split(",")[0])
            q=int(c[2].split(",")[1])
            r=int(c[4].split(",")[0])
            s=int(c[4].split(",")[1])
            for i in range(p,r+1):
                for j in range(q,s+1):
                    a[i][j]=False
                    d[i][j]-=1
                    if d[i][j]==-1:
                        d[i][j]=0
    else:
        p=int(c[1].split(",")[0])
        q=int(c[1].split(",")[1])
        r=int(c[3].split(",")[0])
        s=int(c[3].split(",")[1])
        for i in range(p,r+1):
            for j in range(q,s+1):
                a[i][j]=not a[i][j]
                d[i][j]+=2
light=0
for i in a:
    for j in i:
        if j==True:
            light+=1
print("In the first part no of lights lit is :",light)
light=0
for i in d:
    for j in i:
        light+=j
print("For second part the sum of all brightness value is :",light)
k=input('Press Enter to Exit.')
x.close()
