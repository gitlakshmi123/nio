str = input("enter the string:") 
u=0 
l=0 
n=0 
s=0 
for i in range(len(str)): 
 if( str[i] >= 'A' and str[i] <= 'Z' ):
     u += 1 
 elif( str[i] >= 'a' and str[i] <= 'z' ): 
     l += 1 
 elif( str[i] >= '0' and str[i] <= '9' ): 
     n += 1 
 else: 
     s += 1 
print("given string is:",str) 
print('number of upper case characters:',u) 
print('number of lower case characters:',l) 
print('number of digits:',n) 
print('number of special case characters:',s)
