row=int(input(  "Please input a value"))
for i in range(1,row-1):
    
    if i==1:
       print  ("*"*row)
    for j in range(0,row-1-i):
        print("", end=" ")   
    
    #ın this part hourgloss will complate but it ain't...
    '''
    for j in range(1-i-1,0):
        print("", end=" ") 
    '''
    print("*")
    for j in range(1,row,-1):
        print( 22*" " +" *"*1)
        
for i in range(row,row+1):
    print(  "*"*row)
    for j in range(1-i-1,0):
        print("", end=" ")  
    


    
