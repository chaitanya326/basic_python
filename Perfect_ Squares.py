n=int(input('Enter a number: '))         
def Perfect_Squares(n):
    count=0
    list_of_perfect_squares=[]
    for i in range(n):
        for j in range(i):
            if j*j==i:
                list_of_perfect_squares.append(i)
                count+=1
    print(f'The numbers of perfect squares between 1 and {n} are {count},and the squares are : {list_of_perfect_squares}')
        
Perfect_Squares(n)
