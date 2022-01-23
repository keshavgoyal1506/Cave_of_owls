import hashlib
i=1
flag=False
print('This is a heavy program wait until execution is complete.')
while i>0:
    string='bgvyzdsv'+str(i)
    if flag==False:
        if(hashlib.md5(string.encode('utf-8')).hexdigest()[0:5])=='00000':
            ans=i
            flag=True       
    else:
        if(hashlib.md5(string.encode('utf-8')).hexdigest()[0:6])=='000000':
            ans2=i
            break
    i+=1
print(ans,'is the required number for 5 zeroes in hash.')
print(ans2,'is the required number for 6 zeroes in hash.')
k=input('Press Enter to Exit')
        
    


