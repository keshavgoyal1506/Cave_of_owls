import re
x=open("All Inputs.txt",'r')
while x.readline()!='Day 5\n' :
    continue
n=0
n2=0
for i in range(1000):
    a=x.readline()
    b=re.findall(r"ab|cd|pq|xy+",a)
    if len(b)==0 :
        c=re.findall(r'([a-z])\1*',a)
        if len(c)<16:
            d=re.findall(r'[aeiou]',a)
            if len(d)>=3:
                n+=1
    e=re.findall(r'(\w{2}).*?(\1)',a)
    if len(e)==1:
        f=re.findall(r'(\w).(\1)',a)
        print(f)
    
        if len(f)!=0:
            n2+=1
    else: print(e)
    
        
print('The number of nice strings are',n,n2)
