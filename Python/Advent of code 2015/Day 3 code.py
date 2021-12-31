x=open("All Inputs.txt",'r')
while x.readline()!='Day 3\n' :
    continue
a=x.readline()
b=[(0,0)]
c=[(0,0)]
x=0
y=0
xs=0
ys=0
xr=0
yr=0
for i in range(len(a)-1):#-1 is for new line character
    if a[i]=='<':
        x-=1
        xs-=1-(i%2)
        xr-=i%2
    elif a[i]=='^':
        y+=1
        ys+=1-(i%2)
        yr+=i%2
    elif a[i]=='>':
        x+=1
        xs+=1-(i%2)
        xr+=i%2
    else:
        y-=1
        ys-=1-(i%2)
        yr-=i%2
    b.append((x,y))
    c.append((xr,yr))
    c.append((xs,ys))
print('Santa visited',len(set(b)),'houses at least once.')
print(len(set(c)),'houses were visited by Santa or Robo-Santa at least once.')
k=input('Press enter to Exit.')
x.close()
