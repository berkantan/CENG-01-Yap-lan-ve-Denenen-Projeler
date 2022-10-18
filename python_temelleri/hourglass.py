sıra=23
for i in range(1,23-1):
    
    if i==1:
       print  ("*"*23)
    for j in range(0,sıra-1-i):
        print("", end=" ")   
    
    #ın this part hourgloss will complate but it ain't...
    '''
    for j in range(1-i-1,0):
        print("", end=" ") 
    '''
    print("*")
    for j in range(1,23,-1):
        print( 22*" " +" *"*1)
        
for i in range(23,sıra+1):
    print(  "*"*23)
    for j in range(1-i-1,0):
        print("", end=" ")  
    


    
