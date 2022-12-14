n=int(input('Enter a number: '))         
def Perfect_Squares(n):
    count=0
    lists=[]
    for i in range(n):
        for j in range(i):
            if j*j==i:
                lists.append(i)
                count+=1
    print(f'The numbers of perfect squares between 1 and {n} are {count},and the squares are : {lists}')
        
Perfect_Squares(n)