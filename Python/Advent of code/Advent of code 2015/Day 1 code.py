x=open("All Inputs.txt",'r')
print(x.readline())
a=x.readline()
floor=0
flag=0
for i in range(len(a)):
    if a[i]=='(':
        floor+=1
    else:
        floor-=1
    if floor==-1 and flag==0:
        pos=i+1
        flag+=1   
floor=floor+1#compensating for last new line character.
print('Santa will end up at '+str(floor)+'th floor')
print('Santa will enter basement at '+str(pos)+'th character.')
xmas=input("press enter to exit")
x.close()
