d1 = {'avatar': 2009, 'titanic': 1997, 'starwars': 2015, 'harrypotter': 2011, 'avengers': 2012} 
while(True):
    print("1.ADD 2.DELETE 3.DISPLAY KEYS 4.DISPLAY VALUES 5.DISPLAY BOTH 6.SORT VALUES 7.EXIT") 
    
    
    
    choice = int(input(("enter your choice: "))) 
    if(choice==1):
        key = input("enter the key: ") 
        value = int(input("enter the value: ")) 
        d1[key] = value 
        print(d1) 
    elif(choice==2): 
         print(d1.popitem()) 
         print(d1) 
    elif(choice==3): 
        print(d1.keys()) 
        for x in d1.keys(): 
             print(x) 
    elif(choice==4): 
        print(d1.values()) 
        for x in d1.values():
            print(x) 
    elif(choice==5): 
        print(d1.items()) 
        for x in d1.items(): 
            print(x) 
    elif(choice==6): 
            print(sorted(d1.values())) 
    else: 
         break;
