x=open("All Inputs.txt",'r')
while x.readline()!='Day 7\n' :
    continue
a=[]
b=[]
number=0
for i in range(339):
    a.append(x.readline().split())
for i in a:
    if len(i)==3 :
        b.append(i)
for i in b:
    if i[0][0] not in ['0','1','2','3','4','5','6','7','8','9']:
        b.remove(i)
print(b)

            
