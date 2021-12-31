x=open("All Inputs.txt",'r')
while x.readline()!='Day 2\n' :
    continue    
required=0
ribbon=0
for i in range(1000):
    side=x.readline().split('x')
    side=[int(side[0]),int(side[1]),int(side[2])]
    a=side[0]*side[1]
    b=side[1]*side[2]
    c=side[0]*side[2]
    area=2*a+2*b+2*c
    if side[0]>side[1] :
        if side[0]>side[2]:
            extra=b
            rextra=2*(side[1]+side[2])
        else :
            extra=a
            rextra=2*(side[1]+side[0])
    else:
        if side[1]>side[2]:
            extra=c
            rextra=2*(side[0]+side[2])
        else:
            extra=a
            rextra=2*(side[1]+side[0])
    required+=area+extra
    ribbon+=rextra+side[0]*b
print('The elves need to order',required,'sq.feet of wrapping paper and',ribbon,'feet of ribbon')
k=input('Press enter to exit')
x.close()
